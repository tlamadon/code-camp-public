import scriptflow as sf
import json

# set main options
sf.init({
    # "executors":{
    #     "hpc": {
    #         "maxsize" : 5
    #     } 
    # },
    "executors":{
        "local": {
            "maxsize" : 5
        } 
    },
    'debug':True
})

# define a flow called sleepit
async def flow_mc():

    # prefix = "conda run -n camp "  # if you want to use conda environment
    prefix = ""

    tasks = [
        sf.Task(
            cmd    = [f"{prefix}python scripts/pt_uroot.py -o res_{i}.json -i {i}"],
            shell = True,
            outputs = f"res_{i}.json",
            name   = f"solve-{i}")
        for i in range(10)
    ]

    # we make sure all the tasks are executed
    await sf.bag(*tasks)

    # we combine all outputs into one json
    combined = []
    for t in tasks:
        with open(t.get_outputs()[0]) as f:
            combined.extend(json.load(f))

    with open("res.json", "w") as f:
        json.dump(combined, f, indent=2)


# define a flow called sleepit
async def flow_mc_theta():

    # prefix = "conda run -n camp "  # if you want to use conda environment
    prefix = ""

    tasks = [
        sf.Task(
            cmd    = [f"{prefix}python scripts/pt_uroot.py -o res_{i}.json -i {i}"],
            shell = True,
            outputs = f"res_{i}.json",
            name   = f"solve-{i}")
        for i in range(10)
    ]

    # we make sure all the tasks are executed
    await sf.bag(*tasks)

    # we combine all outputs into one json
    combined = []
    for t in tasks:
        with open(t.get_outputs()[0]) as f:
            combined.extend(json.load(f))

    with open("res.json", "w") as f:
        json.dump(combined, f, indent=2)