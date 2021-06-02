import parent
print(locals())

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("the file is being executed because it is being imported by another file. The file is called:", __name__)