# Main Program to run all the Programs
import json
import divisible_by_5_7
import interleaves_2_strings
import circular_queue


def read_inputs_from_json():
    #C:\Users\sysadmin\PycharmProjects\pythonProject1\main.py
    #C:\Users\sysadmin\PycharmProjects\pythonProject1\input\data.json
    with open(".\data.json") as json_file:
        data = json.load(json_file)
    #print(data)
    return data


if __name__ == '__main__':
    data = read_inputs_from_json()
    print(22*"="+" Inputs "+22*"=")
    print("Given divible_by_5_7_input as ",data["divible_by_5_7_input"])
    print("Given interleaves_strings as ",data["interleaves_strings_inp1"], data["interleaves_strings_inp2"])
    print("Given circular_queue as ",data["queue_inp1"],data["queue_inp2"],data["queue_inp3"],data["queue_inp4"],data["queue_inp5"])

    print(50 * "=")
    print("'program1 execution started', which gives results of divisibility by both 5 and 7")
    divisible_by_5_7.print_divisible_numbers(int(data["divible_by_5_7_input"]))
    print("'program1 execution completed successfully'")
    print(50 * "=")

    print("'program2 execution started', which gives results of interleaves two stings")
    interleaves_2_strings.interleave_strings(data["interleaves_strings_inp1"], data["interleaves_strings_inp2"])
    print("'program2 execution completed successfully'")
    print(50 * "=")

    print("'program3 execution started', which gives results of circularqueue")
    cq = circular_queue.CircularQueue(5)
    cq.enqueue(data["queue_inp1"])
    cq.enqueue(data["queue_inp2"])
    cq.enqueue(data["queue_inp3"])
    cq.enqueue(data["queue_inp4"])
    cq.enqueue(data["queue_inp5"])
    cq.display()
    cq.dequeue()
    cq.display()
    print("'program3 execution completed successfully'")




