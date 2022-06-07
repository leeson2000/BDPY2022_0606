def func30(name, instructor, duration, *args):
    print(f"course name={name}, instructor={instructor}, duration={duration}")
    print(f"  開課時間是:{[t for t in args]}")


periods = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("這個方式有點怪, 注意陣列參數傳入")
func30("BDPY", "Mark", 35, periods)
print("這個方式比較正常, 注意陣列攤平參數傳入")
func30("BDPY", "Mark", 35, *periods)
