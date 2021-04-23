exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_total_minutes = exam_hour * 60 + exam_minute
arrival_total_minutes = arrival_hour * 60 + arrival_minute

if exam_total_minutes - 30 <= arrival_total_minutes <= exam_total_minutes:
    print("On time")
    if exam_total_minutes != arrival_total_minutes:
        diff = exam_total_minutes - arrival_total_minutes
        print(f"{diff} minutes before the start")
elif arrival_total_minutes < exam_total_minutes - 30:
    print("Early")
    diff = exam_total_minutes - arrival_total_minutes
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        diff_h = diff // 60
        diff_m = diff % 60
        if diff_m < 10:
            print(f"{diff_h}:0{diff_m} hours before the start")
        else:
            print(f"{diff_h}:{diff_m} hours before the start")
else:
    print("Late")
    diff = arrival_total_minutes - exam_total_minutes
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        diff_h = diff // 60
        diff_m = diff % 60
        if diff_m < 10:
            print(f"{diff_h}:0{diff_m} hours after the start")
        else:
            print(f"{diff_h}:{diff_m} hours after the start")
