The setattr() function sets the value of the attribute of an object.

The syntax of the setattr() function is:
```python
setattr(object, name, value)
```
Here is a example:

```python
class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

# set value of name to Adam
setattr(person, 'name', 'Adam')
print(person.name)

# set value of marks to 78
setattr(person, 'marks', 78)
print(person.marks)

# Output: 
# Adam
# 78
```
If you want to get the attribute of an object, use getattr().
