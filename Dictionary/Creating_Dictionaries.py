a = dict(key1 = "Value1", key2="Value2", key3="Value3")
print(a)

b={
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
print(b)

c=dict(zip(["key1", "key2", "key3"],["value1","value2","value3"])) #zip([key],[value])
print(c)

d=dict([('key1', 'value1'), ("key2", "value2"), ("key3", "value3")])
print(d)

e=dict({
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
})
print(e)


#pop method

print(e.pop('key2'))
print(e)

#applying list function

x=list(e)
print(x)