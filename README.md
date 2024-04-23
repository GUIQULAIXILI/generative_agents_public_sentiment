

# Base on Generative Agents: Interactive Simulacra of Human Behavior, create a Public Opinion Simulation and Analysis System

<p align="center" width="100%">
<img src="cover.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>

This database is based on "[Generative Agents: Interactive Simulacra of Human Behavior]([joonspk-research/generative_agents: Generative Agents: Interactive Simulacra of Human Behavior (github.com)](https://github.com/joonspk-research/generative_agents))", a system that simulates the generation and analyze of public opinion. Based on the original project, we initialize the personal attributes of the town's agents from external data with public opinion, and utilize the modification of memory nodes, such as adding appropriate fantasies to the memory nodes to create an AI town environment that can generate public opinion. After that, we introduce an expert system for public opinion analysis to facilitate the analysis of public opinion, which in turn affects agent's next plan. At last, we run according to the steps of the original project, and output the results to observe the public opinion propagation.

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Isabella_Rodriguez.png" alt="Generative Isabella">   Setting Up the Environment 
To set up your environment, you will need to generate a `utils.py` file that contains your OpenAI API key and download the necessary packages.

### Step 1. Generate Utils File
In the `reverie/backend_server` folder (where `reverie.py` is located), create a new file titled `utils.py` and copy and paste the content below into the file:
```
# Copy and paste your OpenAI API Key
openai_api_key = "<Your OpenAI API>"
# Put your name
key_owner = "<Name>"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True
```
Replace `<Your OpenAI API>` with your OpenAI API key, and `<name>` with your name.

### Step 2. Install requirements.txt
Install everything listed in the `requirements.txt` file (I strongly recommend first setting up a virtualenv as usual). A note on Python version: we tested our environment on Python 3.9.12. 

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Eddy_Lin.png" alt="Generative Eddy">   API deployment

### Step 1. Install openai package

Set up a new virtualenv and install the lasted openai package.

```
pip install openai
```

### Step 2. Replace API key

Replace `<Your OpenAI API>` with your OpenAI API key in `tuning_model.py`.

```
client = OpenAI(api_key=<Your OpenAI API>)
```

### Step 3. Download and initialize ngrok

If you have already installed and initialized ngrok, you can skip this step.

First visit https://ngrok.com , sign up and download ngrok. Then, unzip the zip file and execute the initialization script.

```
unzip /path/to/ngrok.zip
./ngrok config add=authtoken <your token>
```

You can see your token in your ngrok account.

### Step 4. Ngrok public network deployment

First run `tuning_model.py`.

```
python tuning_model.py
```

Navigate to where ngrok is located  in your command line and run the following command as an administrator:

```
./ngrok http <port number>
```

Please replace `<port number>` with an available port number.

Then, you can get your public network address as follow.

```
Forwarding https://<public network address> -> http://localhost:<port number>
```

### Step 5. Replace public network address

Nagivate to `reverie/backend_server/persona/prompt_template` (this is where `gpt_structure.py` is located). Then Replace `<public network address>` with your public network address in `gpt_structure.py`.

```python
def Expert_system_rumor_request(thought):  
  conn = http.client.HTTPSConnection(<public network address>)  
  payload = json.dumps({  
    "point": "app.external_data_tool.query",  
    "params": {  
      "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",  
      "tool_variable": "rumor_retrieve",  
      "inputs": {  
        "content": thought  
      },  
      "query": "what the rumor will be?"  
    }  
  })  
  headers = {  
    'Authorization': 'Bearer 123456',  
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',  
    'Content-Type': 'application/json'  
  }  
  conn.request("POST", "/api/rumorGen/receive", payload, headers)  
  res = conn.getresponse()  
  data = res.read()  
  print(data.decode("utf-8"))  
  return data.decode("utf-8")
```

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Maria_Lopez.png" alt="Generative Maria">   Creating Agents Templates

In order to create a group with public opinion propagation, we need to utilize some data such as the comments of videos or articles , etc. to create agents groups accordingly. So that different agent's personalities will be generated by utilizing different comment data, which will enable us to simulate the propagation of public opinion in different environments.

### Step 1. Get comment data

In the folder `reverie/backend_server/generateAgentByBsite`, save the comments which can be collected by the web crawler or  simulated on your own as a json file here (named `ori_comment.json` in this project), or if saved as a csv file (named `comments .csv`), you can run `datas.py` to convert the csv file to a json file.

Finally, in the json file should ensure that each piece of data in the attributes must have "content" and "sex", after the work of these two attributes are indispensable, other attributes can be added by yourself.

### Step 2. Initialize agent data

After saving the comment data in a json file, in the `reverie/backend_server/generateAgentByBsite` directory, we generate an agent's base data based on each piece of data by running the following command:

```
python handle_data.py
```

By default, we only generate data for 10 agents, if you want to modify it to get more agent templates, you can do so by modifying the loop count in the loop code block of `handle_data.py`, provided that the comment data you got in the first step is enough for you to generate the corresponding number of agent templates.

Then run the following command afterward:

```
python init_environment.py
python init_person.py
python init_person_data.py
python init_reverie.py
```

After that, the initialized agent data will be saved in four folders,which are  `generateAgentByBsite/environment`, `generateAgentByBsite/movement`, `generateAgentByBsite/personas`, `generateAgentByBsite/reverie`, and thus the agent templates with the opinion data will be created.

### Step 3. Save agent data

Finally, create a new custom folder in `environment/frontend_server/storage`, for example, you can name it `base_the_ville_rumor`, and then copy and paste the four folders that you have just initialized in `generateAgentByBsite` into ` base_the_ville_rumor`, and then the agent template with opinion data will be saved.

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Klaus_Mueller.png" alt="Generative Klaus">   Running a Simulation 
To run a new simulation, you will need to concurrently start two servers: the environment server and the agent simulation server.

### Step 1. Starting the Environment Server
Again, the environment is implemented as a Django project, and as such, you will need to start the Django server. To do this, first navigate to `environment/frontend_server` (this is where `manage.py` is located) in your command line. Then run the following command:

    python manage.py runserver

Then, on your favorite browser, go to [http://localhost:8000/](http://localhost:8000/). If you see a message that says, "Your environment server is up and running," your server is running properly. Ensure that the environment server continues to run while you are running the simulation, so keep this command-line tab open! (Note: I recommend using either Chrome or Safari. Firefox might produce some frontend glitches, although it should not interfere with the actual simulation.)

### Step 2. Starting the Simulation Server
Open up another command line (the one you used in Step 1 should still be running the environment server, so leave that as it is). Navigate to `reverie/backend_server` and run `reverie.py`.

    python reverie.py
This will start the simulation server. A command-line prompt will appear, asking the following: "Enter the name of the forked simulation: ". To start a simulation with the agent template you just created on previous step, type the following:
    base_the_ville_rumor
The prompt will then ask, "Enter the name of the new simulation: ". Type any name to denote your current simulation (e.g., just "test-simulation" will do for now).

    test-simulation
Keep the simulator server running. At this stage, it will display the following prompt: "Enter option: "

### Step 3. Running and Saving the Simulation
On your browser, navigate to [http://localhost:8000/simulator_home](http://localhost:8000/simulator_home). You should see the map of Smallville, along with a list of active agents on the map. You can move around the map using your keyboard arrows. Please keep this tab open. To run the simulation, type the following command in your simulation server in response to the prompt, "Enter option":

    run <step-count>
Note that you will want to replace `<step-count>` above with an integer indicating the number of game steps you want to simulate. For instance, if you want to simulate 100 game steps, you should input `run 100`. One game step represents 10 seconds in the game.


Your simulation should be running, and you will see the agents moving on the map in your browser. Once the simulation finishes running, the "Enter option" prompt will re-appear. At this point, you can simulate more steps by re-entering the run command with your desired game steps, exit the simulation without saving by typing `exit`, or save and exit by typing `fin`.

The saved simulation can be accessed the next time you run the simulation server by providing the name of your simulation as the forked simulation. This will allow you to restart your simulation from the point where you left off.

### Step 4. Replaying a Simulation
You can replay a simulation that you have already run simply by having your environment server running and navigating to the following address in your browser: `http://localhost:8000/replay/<simulation-name>/<starting-time-step>`. Please make sure to replace `<simulation-name>` with the name of the simulation you want to replay, and `<starting-time-step>` with the integer time-step from which you wish to start the replay.

For instance, by visiting the following link, you will initiate a pre-simulated example, starting at time-step 1:  
[http://localhost:8000/replay/July1_the_ville_isabella_maria_klaus-step-3-20/1/](http://localhost:8000/replay/July1_the_ville_isabella_maria_klaus-step-3-20/1/)

### Step 5. Demoing a Simulation
You may have noticed that all character sprites in the replay look identical. We would like to clarify that the replay function is primarily intended for debugging purposes and does not prioritize optimizing the size of the simulation folder or the visuals. To properly demonstrate a simulation with appropriate character sprites, you will need to compress the simulation first. To do this, open the `compress_sim_storage.py` file located in the `reverie` directory using a text editor. Then, execute the `compress` function with the name of the target simulation as its input. By doing so, the simulation file will be compressed, making it ready for demonstration.

To start the demo, go to the following address on your browser: `http://localhost:8000/demo/<simulation-name>/<starting-time-step>/<simulation-speed>`. Note that `<simulation-name>` and `<starting-time-step>` denote the same things as mentioned above. `<simulation-speed>` can be set to control the demo speed, where 1 is the slowest, and 5 is the fastest. For instance, visiting the following link will start a pre-simulated example, beginning at time-step 1, with a medium demo speed:  
[http://localhost:8000/demo/July1_the_ville_isabella_maria_klaus-step-3-20/1/3/](http://localhost:8000/demo/July1_the_ville_isabella_maria_klaus-step-3-20/1/3/)

### Tips
We've noticed that OpenAI's API can hang when it reaches the hourly rate limit. When this happens, you may need to restart your simulation. For now, we recommend saving your simulation often as you progress to ensure that you lose as little of the simulation as possible when you do need to stop and rerun it. Running these simulations, at least as of early 2023, could be somewhat costly, especially when there are many agents in the environment.

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Maria_Lopez.png" alt="Generative Maria">   Simulation Storage Location
All simulations that you save will be located in `environment/frontend_server/storage`, and all compressed demos will be located in `environment/frontend_server/compressed_storage`. 

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Sam_Moore.png" alt="Generative Sam">   Customization

There are two ways to optionally customize your simulations. 

### Author and Load Agent History
First is to initialize agents with unique history at the start of the simulation. To do this, you would want to 1) start your simulation using one of the base simulations, and 2) author and load agent history. More specifically, here are the steps:

#### Step 1. Starting Up a Base Simulation 
There are one base simulations included in the original repository: `base_the_ville_isabella_maria_klaus` . Load this base simulations by following the steps until step 2 above. 

#### Step 2. Loading a History File 
Then, when prompted with "Enter option: ", you should load the agent history by responding with the following command:

    call -- load history the_ville/<history_file_name>.csv
Note that you will need to replace `<history_file_name>` with the name of an existing history file. There are two history files included in the repo as examples: `agent_history_init_n25.csv` for `base_the_ville_n25` and `agent_history_init_n3.csv` for `base_the_ville_isabella_maria_klaus`. These files include semicolon-separated lists of memory records for each of the agents—loading them will insert the memory records into the agents' memory stream.

#### Step 3. Further Customization 
To customize the initialization by authoring your own history file, place your file in the following folder: `environment/frontend_server/static_dirs/assets/the_ville`. The column format for your custom history file will have to match the example history files included. Therefore, we recommend starting the process by copying and pasting the ones that are already in the repository.

### Create New Base Simulations
For a more involved customization, you will need to author your own base simulation files. The most straightforward approach would be to copy and paste an existing base simulation folder, renaming and editing it according to your requirements. This process will be simpler if you decide to keep the agent names unchanged. However, if you wish to change their names or increase the number of agents that the Smallville map can accommodate, you might need to directly edit the map using the [Tiled](https://www.mapeditor.org/) map editor.


## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Eddy_Lin.png" alt="Generative Eddy">   Authors and Citation 

**Authors:** Jiahao He, Bixin Li, Juntian Huang, Dingming Li

Please cite our paper if you use the code or data in this repository. 
```
@inproceedings{Park2023GenerativeAgents,  
author = {Park, Joon Sung and O'Brien, Joseph C. and Cai, Carrie J. and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S.},  
title = {Generative Agents: Interactive Simulacra of Human Behavior},  
year = {2023},  
publisher = {Association for Computing Machinery},  
address = {New York, NY, USA},  
booktitle = {In the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)},  
keywords = {Human-AI interaction, agents, generative AI, large language models},  
location = {San Francisco, CA, USA},  
series = {UIST '23}
}
```

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Wolfgang_Schulz.png" alt="Generative Wolfgang">   Acknowledgements

We encourage you to support the following three amazing artists who have designed the game assets for this project, especially if you are planning to use the assets included here for your own project: 
* Background art: [PixyMoon (@_PixyMoon\_)](https://twitter.com/_PixyMoon_)
* Furniture/interior design: [LimeZu (@lime_px)](https://twitter.com/lime_px)
* Character design: [ぴぽ (@pipohi)](https://twitter.com/pipohi)

In addition, we thank Lindsay Popowski, Philip Guo, Michael Terry, and the Center for Advanced Study in the Behavioral Sciences (CASBS) community for their insights, discussions, and support. Lastly, all locations featured in Smallville are inspired by real-world locations that Joon has frequented as an undergraduate and graduate student---he thanks everyone there for feeding and supporting him all these years.

