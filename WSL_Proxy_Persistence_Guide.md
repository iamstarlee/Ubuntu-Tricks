# WSL 代理持久化与故障排查指南

本文用于解决以下问题：Windows 或 WSL 升级、电脑重启后，WSL 中的代理失效，导致 `curl`、包管理器及其他命令行程序无法联网。

## 1. 推荐结构

推荐使用 Windows 11 的 WSL 镜像网络：

```text
WSL 程序 → 127.0.0.1:7897 → Windows 代理程序 → Internet
```

本文示例中的 HTTP 代理端口为 `7897`。如果代理软件使用其他端口，需要把命令中的 `7897` 替换为实际端口。

## 2. Windows 侧配置

### 2.1 配置 WSL 镜像网络和自动代理

在 Windows PowerShell 中运行：

```powershell
notepad $env:USERPROFILE\.wslconfig
```

写入以下内容：

```ini
[wsl2]
networkingMode=mirrored
autoProxy=true
dnsTunneling=true
```

保存后，在 PowerShell 中完全关闭 WSL：

```powershell
wsl --shutdown
```

然后重新打开 WSL。

这些选项的作用：

- `networkingMode=mirrored`：让 WSL 能通过 `127.0.0.1` 访问 Windows 上监听的服务。
- `autoProxy=true`：把 Windows 的 HTTP 代理配置自动注入 WSL。
- `dnsTunneling=true`：改善 VPN、代理和复杂网络环境中的 DNS 兼容性。

### 2.2 设置代理软件随 Windows 启动

在 Windows 代理软件中确认：

- 已开启开机自启动。
- HTTP 代理端口仍为 `7897`。
- Windows 系统代理已开启。
- 如果使用 WSL NAT 网络而非镜像网络，需要开启“允许局域网连接”，并检查 Windows 防火墙。

## 3. WSL 侧检查

重新打开 WSL 后，运行：

```bash
env | grep -iE '^(http_proxy|https_proxy|all_proxy|no_proxy)='
```

预期结果类似：

```text
HTTP_PROXY=http://127.0.0.1:7897
HTTPS_PROXY=http://127.0.0.1:7897
http_proxy=http://127.0.0.1:7897
https_proxy=http://127.0.0.1:7897
NO_PROXY=localhost,127.0.0.1,::1
no_proxy=localhost,127.0.0.1,::1
```

如果 `~/.bashrc` 等文件中查不到这些配置，但 `env` 中存在，说明它们很可能由 WSL 的 `autoProxy=true` 自动注入，这是正常现象。

检查常见配置文件中是否存在旧代理：

```bash
rg -n '7891|7897|HTTP_PROXY|HTTPS_PROXY|ALL_PROXY' \
  ~/.bashrc ~/.profile ~/.zshrc /etc/environment 2>/dev/null
```

如果同时存在以下两类配置：

```text
HTTP_PROXY=http://127.0.0.1:7897
ALL_PROXY=socks5://127.0.0.1:7891
```

不同程序可能选择不同代理。若没有明确的 SOCKS5 使用需求，建议删除旧的 `ALL_PROXY` 设置，统一使用 HTTP 代理。

## 4. 手动配置作为备用方案

如果 `autoProxy=true` 没有自动注入环境变量，可以在 `~/.bashrc` 末尾加入：

```bash
export HTTP_PROXY="http://127.0.0.1:7897"
export HTTPS_PROXY="http://127.0.0.1:7897"
export http_proxy="$HTTP_PROXY"
export https_proxy="$HTTPS_PROXY"

unset ALL_PROXY
unset all_proxy

export NO_PROXY="localhost,127.0.0.1,::1"
export no_proxy="$NO_PROXY"
```

应用配置：

```bash
source ~/.bashrc
```

注意：如果环境变量由 WSL 自动注入，就不必在 `~/.bashrc` 中重复配置。

## 5. 验证代理是否成功

### 5.1 查看环境变量

```bash
env | grep -i proxy
```

### 5.2 查看到代理端口的连接

先执行一次网络请求，再运行：

```bash
ss -nt | grep -E '7891|7897'
```

出现类似结果表示 WSL 正在连接 Windows 代理：

```text
ESTAB 0 0 127.0.0.1:47240 127.0.0.1:7897
```

### 5.3 查看代理出口地区

```bash
curl -sS --max-time 15 \
  https://www.cloudflare.com/cdn-cgi/trace |
grep -E '^(ip|loc|colo)='
```

示例：

```text
ip=94.177.131.236
colo=NRT
loc=JP
```

这表示请求已经通过代理出口访问网络。

### 5.4 验证普通 HTTPS 网站

```bash
curl -I --max-time 15 https://www.cloudflare.com
```

正常情况下会先看到代理建立隧道：

```text
HTTP/1.1 200 Connection established
```

随后看到目标网站返回：

```text
HTTP/2 200
```

两者同时出现表示 HTTPS 代理工作正常。

### 5.5 验证 OpenAI API 的网络连通性

```bash
curl -sS -o /dev/null \
  -w 'HTTP=%{http_code} CONNECT=%{time_connect}s TOTAL=%{time_total}s\n' \
  --connect-timeout 10 --max-time 25 \
  https://api.openai.com/v1/models
```

未携带 API Key 时，返回以下结果说明网络已经到达 API，只是请求没有认证：

```text
HTTP=401
```

常见结果含义：

| 结果 | 含义 |
| --- | --- |
| `HTTP=401` | 已到达服务器，但没有有效认证信息 |
| `HTTP=403` | 服务器拒绝请求，需要查看返回正文中的具体原因 |
| `HTTP=000` | 没有收到 HTTP 响应，通常是连接、DNS 或代理问题 |
| `curl: (28)` | 请求超时 |

## 6. 重启后快速检查顺序

电脑重启后，如果 WSL 无法联网，按以下顺序检查：

1. 确认 Windows 代理软件已经启动。
2. 确认代理端口仍为 `7897`。
3. 确认 Windows 系统代理已开启。
4. 在 WSL 中检查 `env | grep -i proxy`。
5. 用 Cloudflare trace 检查出口 IP 和地区。
6. 用 `ss -nt` 检查是否连接到 `127.0.0.1:7897`。
7. 用 `curl -I` 检查 HTTPS 是否能返回状态码。
8. 如果修改了 `.wslconfig`，执行 `wsl --shutdown` 后重新启动 WSL。

## 7. 常见问题

### 7.1 `127.0.0.1:7897` 显示 Connection refused

可能原因：

- Windows 代理软件没有启动。
- 代理软件端口发生变化。
- WSL 没有使用镜像网络。
- Windows 防火墙或安全软件拦截连接。

先在 PowerShell 中检查 `.wslconfig`，再执行：

```powershell
wsl --shutdown
```

### 7.2 `env` 有代理，但 `rg` 查不到配置

这通常表示代理变量由 WSL 的 `autoProxy=true` 自动注入。只要网络测试正常，无需在 `~/.bashrc` 中重复添加。

### 7.3 `curl` 可以联网，但某个程序仍然超时

可能原因：

- 程序不读取 `HTTP_PROXY` 或 `HTTPS_PROXY`。
- 程序优先读取了旧的 `ALL_PROXY`。
- 程序需要 WebSocket，而代理中断了长连接。
- 程序已进入认证、额度、权限或地区检查阶段。

此时应查看该程序的完整错误信息。网络能返回 HTTP 状态码，只能说明网络链路建立成功，不代表认证、账户额度或服务权限正常。

## 8. 当前验证成功的参考状态

本次成功验证时使用：

```text
HTTP_PROXY=http://127.0.0.1:7897
HTTPS_PROXY=http://127.0.0.1:7897
ALL_PROXY 未设置
代理出口 loc=JP
Cloudflare 返回 HTTP/2 200
WSL 到 127.0.0.1:7897 存在 ESTAB 连接
```

只要重启后仍满足以上条件，就可以确认 WSL 代理配置正常。
