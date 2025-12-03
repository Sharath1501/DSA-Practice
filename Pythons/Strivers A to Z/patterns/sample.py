from threading import Thread, Condition

cond = Condition()
done = 1

def task(name):
    global done
    with cond:  # Use the condition with proper acquire/release management
        if done == 1:
            done = 2
            print("Executing t1:", name)
            cond.wait()  # Wait until notified
            print("Condition met:", name)
        else:
            for i in range(5):
                print(".")
            print("Executing t2:", name)
            cond.notify_all()  # Notify all waiting threads
            print("Done with thread t2:", name)

if __name__ == '__main__':
    t1 = Thread(target=task, args=('t1',))  # Pass the argument as a tuple
    t2 = Thread(target=task, args=('t2',))  # Fix the argument for t2

    t1.start()
    t2.start()
    t1.join()
    t2.join()
