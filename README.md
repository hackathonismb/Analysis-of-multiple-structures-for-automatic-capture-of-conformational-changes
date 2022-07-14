# Analysis Of Multiple Structures For Automatic Capture of Conformational Changes
## Tools for Analyzing Structural Sets- Exploring Protein Conformations 

### Task 
We are developing sensitive methods to detect subtle differences between protein structures, by leveraging large datasets and expanding iCn3D distance functions analysis feature. As a result, we may identify different interactions which can cause difference in structures. Recognizing different structures will allow us to dig deeper and determine mechanisms that cause the difference.

### Workflow Description
In the iCn3D command line, input their structure name and defined sets command for distance set analysis. Users may use proteinset_command.py to generate this command. Next, in iCn3D, select Analysis > Distance > Among Many Sets and save the generated table as an HTML file. The HTML file can then be run on [INSERT SCRIPT NAME] that will parse the HTML file information, gather distances for all possible combinations of sets, and compile output to a table mapping structure identification to distance vector. The output table should be saved as a CSV file and run cluster.py to cluster data and generate a dendrogram. 

### Workflow Diagram 

### Applications 
- Evaluate experimental structures in reference to AlphaFold structures
- Understand variations in protein conformation within families
- Analysis of molecular dynamics trajectories
- Discern subtle conformational differences eliduded by large dataset analysis


### Tutorial 



### Future Add-Ons
- Create an interactive Dendrogram and intergrate the figure to iCn3D
- Expand analysis parameters to handle arbitrary alignments such as different chain identifers and different residue numbering between structures 


**Team:**
- Tom Madej (Team Lead),[madej@ncbi.nlm.nih.gov](url)
- David Bell, [david.bell@nih.gov](url)
- Chase Freschlin, [freschlin@wisc.edu](url)
- Gabby Vent, [christopher.vento@rockets.utoledo.edu](url)
- Lianna Khachikyan,[lianna.khachikyan.348@my.csun.edu](url)

