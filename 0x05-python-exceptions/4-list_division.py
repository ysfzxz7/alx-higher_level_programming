#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lis = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            lis.append(result)
        except ZeroDivisionError as e:
            print("division by 0")
            lis.append(0)
        except (TypeError, ValueError) as e:
            print("wrong type")
            lis.append(0)
        except IndexError as e:
            print("out of range")
            lis.append(0)
        finally:
            continue
    return (lis)


if __name__ == "__main__":
    list_division()
