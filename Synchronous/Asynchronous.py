import asyncio
import time
# async def fetch_data(delay):
#   print("Fetching data")
#   await asyncio.sleep(delay)
#   print("Data fetched")
#   return {"data":"Some Data"}
 
# async def main():
#   print("Start of main coroutine")
#   tf = time.timezone
#   task = fetch_data(3)
#   result = await task
#   ts = time.timezone
#   print(f"Received Result:{result}")
#   print("End of Main coroutine")  
  
 
#   print(f"time taken:{ts}-{tf}")
  
# asyncio.run(main())  



# async def fetch_data(delay):
#   print("Fetching data")
#   await asyncio.sleep(delay)
#   print("Data fetched")
#   return {"data":"Some Data"}
# async def main():
#   print("Start of main coroutine")
#   task = fetch_data(3)
#   print("End of Main coroutine") 
#   result = await task
#   print(f"Received Result:{result}")
  
  
# asyncio.run(main())  


# async def fetch_data(id,sleep_time):
#   print(f"Coroutine{id} Startitng the data")
#   await asyncio.sleep(sleep_time)
#   return {"id":id,"data":f"Sample data from coroutine{id}"}
# async def main():
#   task1 = asyncio.create_task(fetch_data(1,2))
#   task2 = asyncio.create_task(fetch_data(2,3))
#   task3 = asyncio.create_task(fetch_data(3,4))
#   result1 = await task1
#   result2 = await task2
#   result3 = await task3
#   print(result1,result2,result3)

# asyncio.run(main())



# async def fetch_data(id,sleep_time):
#   print(f"Coroutine{id} Startitng the data")
#   await asyncio.sleep(sleep_time)
#   return {"id":id,"data":f"Sample data from coroutine{id}"}
# async def main():
#   # gather function
#  results = await asyncio.gather(fetch_data(1,2),fetch_data(1,2),fetch_data(1,2))
#  for result in results:
#   print(f"Recieved results{result}")
# asyncio.run(main())


# TaskGroup
# async def fetch_data(id,sleep_time):
#   print(f"Coroutine{id} Startitng the data")
#   await asyncio.sleep(sleep_time)
#   return {"id":id,"data":f"Sample data from coroutine{id}"}

# async def main():
#   tasks = []
#   async with asyncio.TaskGroup() as tg:
#     for i, sleep_time in enumerate([2,1,3],start=1):
#       task=tg.create_task(fetch_data(i,sleep_time))
#       tasks.append(task)
#   results=  [task.result() for task in tasks] 
#   for result in results:
#     print(f'Recieved Result:{result}') 
# asyncio.run(main())       
    
    
    # future 
# async def set_future_result(future,value):
#   await asyncio.sleep(2)
#   future.set_result(value)
#   print(f"Set the future's result to:{value}")
  
# async def main():
#   loop = asyncio.get_running_loop()
#   future = loop.create_future()
#   asyncio.create_task(set_future_result(future,"Future is Ready"))
#   result =  await future  
#   print(f"Recieved the future Result's:{result}")
# asyncio.run(main()) 



# Event Function

async def waiter(event):
  print(f"Waiting for the event to be set")
  await event.wait()
  print("Event has been set, continuing Execution")
  
  
async def setter(event):
  
  print("Before Event Set")
  await asyncio.sleep(3)
  event.set()
  print("Event has been set") 
async def main():
      event = asyncio.Event()
      await asyncio.gather(waiter(event),setter(event))
asyncio.run(main())      