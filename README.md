# Table of contents
- [General Description](#General-Information)
- [Folder Description](#Navigating-the-Folders)
- [Execution Information](#Execution-Information)
- [The Team](#The-Team)

# General-Information
This repository contains the final results of efforts made to complete the final project of the class **EEL5718**, Computer Communications, in the **Fall 2025 - 2026 EDGE semester**. It contains the combined efforts of all memebers, Ben, Devin, and Blake, to benchmard different network topologies using different performance metrics and different communication protocols. 

# Navigating-the-Folders
The folder structure for the project goes as follows:
- **CyclicTopoFiles - Fixed** contains the Python files setting up the cyclic topologies (mesh, star, hybrid, and ring) to demonstrate comparable performance to the **FinalProjectTopologies** directory. The only change (different from the below *CyclicTopoFiles - Unfixed* is that link limitation parameters have been removed.
- **CyclicTopoFiles - Unfixed** contains the Python files setting up the cyclic topologies (mesh, star, hybrid, and ring) to demonstrate comparable raw performance *directly* reflecting the topology configuration in the base topology layout. This means that each topology has the exact same configuration and has only been edited to be executed via the CLI.
- **BaseTopoFiles** contains the subdirectories for each topology. Each subdirectory (linear, tree, mesh, star, hybrid, and ring) contain the *python* and the *mn* files of our network topology configurations.

# Execution-Information
To run each topology, you can do as follows.

## Cyclic Topology Files
This section describes the execution protocol for **BOTH** fixed and unfixed cyclic topology networks (mesh, ring, star, hybrid). 

1. Ensure that no network configuration exists by running: ```sudo mn -c``` to clear the previous network configuration (if it exists).
2. Then, execute the file by running ```sudo mn python3 'desired_topology_file_name`.py``` and wait for the pingAll command to finish executing. **NOTE**, replace 'desired_topology_file_name'.py with (of course) your desired topology. An example would be: ```sudo mn python3 eel5718_ring_topology.py```.
3. Once the pingAll is complete, and all nodes have achieved their ARP, you can run: ```xterm 'desired host name'``` to open a CLI for the host that you desire. To replicate tests, you can run the following (for example): ```xterm h1 h2 h15```.
4. Once you have a CLI open for your desired host, you can choose one to function as the server, and then the other two to function as the client. Notice in my above example that I chose **h1, h2, and h15**. H1 and H2 are close, H1 and H15 are far, thus, H1 or H2 can be the server. The latter can be the close client and H15 can be the far client.

## Non-Cyclic Topology Files
This section describes the execution protocol for non-cyclic topology networks (linear and tree). These are separated to address the *MiniEdit* tool's issues with running cyclic topologies via the GUI. 

1. To test cyclic (mesh, hybrid, ring, star) topology performance run the following **IN ORDER**.
- On H1: ```ifconfig``` and note the IP. Then run: ```iper3```.
- On H2 and H15 for *UDP* (bandwidth, packetloss and jitter): ```iperf3 -c 'host ip' -u -b 100M -t 60```. For the same benchmark, but for *TCP*, run ```iperf3 -c 'host ip' -b 100M -t 60```
2. To Test non-cyclic (linear and tree) topology performance, you can do so via the MiniEdit GUI. To do so, run: ```sudo python3 'path_to_your_miniedit_file'/MiniEdit.py``` and then open the downloaded files using the GUI tool.
- **NOTE**: Our group noticed some issues with importing .mn files. Thus, please reference this [source](https://github.com/mininet/mininet/issues/1214) for information on how to resolve if you encounter import issues.
3. Once the topology is running as expected, just right click on the desired hosts (adhering to the server, close to server, and far from server nodes) and run the exact commands listed in the subsection of poiunt **5**.


# The-Team
Benjamin Simonson - bsimonson@ufl.edu
Devin Dykstra - devindykstra@ufl.edu 
Blake Sanders - blake.sanders@ufl.edu 
