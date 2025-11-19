age: int = 20
age = "Michał"


def create_me_a_picture(elements: list[str], colors: list[int]) -> int | None:
    for element in elements:
        print(element)
    if "football" in elements:
        return None
    return len(colors)

create_me_a_picture(["pizza", "czlowiek"], "green")

# create_me_a_picture(12, ["green", "blue"])