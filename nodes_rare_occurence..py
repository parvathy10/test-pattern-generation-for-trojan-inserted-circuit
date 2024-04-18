#!/usr/bin/env python
# coding: utf-8

# In[17]:


def calculate_probabilities(netlist):
    node_probabilities = {}
    
    # Initialize input nodes with probability 0.5
    for input_node in netlist['inputs']:
        node_probabilities[input_node] = {'zero_prob': 0.5, 'one_prob': 0.5}
    
    # Calculate probabilities for each gate
    for gate, (gate_type, inputs) in netlist['gates'].items():
        # Calculate probability of the gate's output
        output_zero_prob = 1.0
        output_one_prob = 1.0
        for input_node in inputs:
            input_prob = node_probabilities[input_node]
            output_zero_prob *= (1 - input_prob['one_prob']) 
            output_one_prob *= (1 - input_prob['zero_prob']) 
        
        # Store the probabilities of the gate's output
        node_probabilities[gate] = {'zero_prob': output_zero_prob, 'one_prob': output_one_prob}
    
    return node_probabilities

def find_nodes_below_threshold(probabilities, theta):
    #create an empty list
    nodes_below_threshold = []
    # Iterate over each node and its probabilities in the given dictionary
    for node, probab in probabilities.items():
        # Check if either zero or one probability is below the threshold
        if probab['zero_prob'] < theta or probab['one_prob'] < theta:
            # If below threshold, add the node to the list
            nodes_below_threshold.append(node)
    return nodes_below_threshold

# Define the netlist representation of the ISCAS85 c17 circuit
circuit_netlist = {
    'inputs': ['N1', 'N2', 'N3', 'N6', 'N7'],
    'gates': {
        'N10': ('NAND', ['N1', 'N3']),
        'N11': ('NAND', ['N3', 'N6']),
        'N16': ('NAND', ['N11', 'N2']),
        'N19': ('NAND', ['N11', 'N7']),
        'N22': ('NAND', ['N10', 'N16']),
        'N23': ('NAND', ['N19', 'N16'])
    }
}

def to_find_nodes_below_threshold(probabilities, theta):
    nodes_below_threshold = []
    # Iterate over each pair of nodes in the given dictionary
    for node1, probs1 in probabilities.items():
        for node2, probs2 in probabilities.items():
            # Avoid multiplying the same node
            if node1 != node2:
                # Calculate the product of probabilities for zero and one
                product_zero = probs1['zero_prob'] * probs2['zero_prob']
                product_one = probs1['one_prob'] * probs2['one_prob']
                # Check if any product is below the theta
                if product_zero < theta or product_one < theta:
                    nodes_below_threshold.append((node1, node2))
    return nodes_below_threshold

# Calculate probabilities for each node
node_probabilities = calculate_probabilities(circuit_netlist)

# Set the theta value
theta = 0.07

# Find nodes with probabilities below the theta
nodes_below_threshold = find_nodes_below_threshold(node_probabilities, theta)

# Print probabilities of each node
print("Node Probabilities:")
for node, probab in node_probabilities.items():
    print(f"{node}: Zero Probability - {probab['zero_prob']}, One Probability - {1 - probab['zero_prob']}")

# Print nodes below the theta
print("\nNodes with Probabilities below Threshold:")
print(nodes_below_threshold)
print("\n")

node_combinations_below_threshold = to_find_nodes_below_threshold(node_probabilities, theta)

#Print node combinations with probabilities below the theta
print("Node Combinations with Probabilities below Threshold:")
for node_combination in node_combinations_below_threshold:
    print(f"Combination: {node_combination}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




