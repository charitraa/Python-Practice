class parentclass:
    def parent_method(self):
        print("parent method")


class childclass(parentclass):
    def child_method(self):
        print("thsi is the child")
        super().parent_method()


child_object = childclass()
child_object.parent_method()
