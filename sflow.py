import scriptflow as sf

# set main options
sf.init({
    "executors":{
        "hpc": {
            "maxsize" : 5
        } 
    },
    'debug':True
})

# example of a simple step that combines outcomes
def step2_combine_file():
    with open('test_1.txt') as f:
        a = int(f.readlines()[0])
    with open('test_2.txt') as f:
        b = int(f.readlines()[0])
    with open('final.txt','w') as f:
        f.write("{}\n".format(a+b))

# define a flow called sleepit
async def flow_sleepit():

    i=1
    task1 = sf.Task(
      cmd    = [f"conda run -n camp python scripts/pt_uroot.py > test_{i}.txt"],
      shell = True,
      outputs = f"test_{i}.txt",
      name   = f"solve-{i}")

    i=2
    task2 = sf.Task(
      cmd    = [f"conda run -n camp python scripts/pt_uroot.py > test_{i}.txt"],
      shell = True,
      outputs = f"test_{i}.txt",
      name   = f"solve-{i}")

    await sf.bag(task1,task2)

    task_final = sf.Task(
      cmd = "python -c 'import sflow; sflow.step2_combine_file()'",
      outputs = f"final.txt",
      inputs = [*task1.get_outputs(),*task2.get_outputs()])

    await task_final
