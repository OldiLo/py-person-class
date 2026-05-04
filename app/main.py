class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    ppl_list = []
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        name = person["name"]
        instance = Person.people[name]

        spouse_type = "wife" if person.get("wife") else "husband"
        spouse_name = person.get(spouse_type)

        if spouse_name is not None:
            setattr(instance, spouse_type, Person.people[spouse_name])

        ppl_list.append(instance)

    return ppl_list
