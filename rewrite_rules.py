from qiskit.transpiler.basepasses import TransformationPass
from qiskit.dagcircuit import DAGCircuit
from qiskit.dagcircuit.dagnode import DAGOpNode

class GPI2_Adjoint(TransformationPass):
    def run(self, dag: DAGCircuit) -> DAGCircuit:
        nodes_to_remove = []

        for node in dag.op_nodes():
            if isinstance(node, DAGOpNode) and node.op.name == 'gpi2':
                #print(f"Found gpi2 node: {node}, params: {node.op.params}")
                successors = [succ for succ in dag.quantum_successors(node) if isinstance(succ, DAGOpNode)]
                for next_node in successors:
                    if next_node.op.name == 'gpi2' and node.qargs == next_node.qargs:
                        phi1 = node.op.params[0]
                        phi2 = next_node.op.params[0]
                        if (phi2 + 0.5) % 1 == phi1 % 1 or (phi1 + 0.5) % 1 == phi2 % 1:
                            #print(f"Removing gpi2 nodes: {node} and {next_node}")
                            nodes_to_remove.extend([node, next_node])
                            
        for node in nodes_to_remove:
            dag.remove_op_node(node)
        
        return dag
    
    
class CancelFourGPI2(TransformationPass):
    def run(self, dag: DAGCircuit) -> DAGCircuit:
        nodes_to_remove = []
        gpi2_streak = []

        for node in dag.topological_op_nodes():
            if node.op.name == 'gpi2' and node.op.params == [0.5]:  # GPI2(pi)
                gpi2_streak.append(node)
                if len(gpi2_streak) == 4:
                    #print(f"Found four consecutive gpi2 nodes: {gpi2_streak}")
                    nodes_to_remove.extend(gpi2_streak)
                    gpi2_streak = []
            else:
                gpi2_streak = []

        for node in nodes_to_remove:
            dag.remove_op_node(node)

        return dag

class GPI_Adjoint(TransformationPass):
    def run(self, dag: DAGCircuit) -> DAGCircuit:
        nodes_to_remove = []

        for node in dag.op_nodes():
            if isinstance(node, DAGOpNode) and node.op.name == 'gpi':
               #print(f"Found gpi node: {node}, params: {node.op.params}")
                successors = [succ for succ in dag.quantum_successors(node) if isinstance(succ, DAGOpNode)]
                for next_node in successors:
                    if next_node.op.name == 'gpi' and node.qargs == next_node.qargs:
                        phi1 = node.op.params[0]
                        phi2 = next_node.op.params[0]
                        if phi2 == phi1:
                            #print(f"Removing gpi nodes: {node} and {next_node}")
                            nodes_to_remove.extend([node, next_node])
                            

        for node in nodes_to_remove:
            dag.remove_op_node(node)
        
        return dag

class CommuteGPI2MS(TransformationPass):
    def run(self, dag: DAGCircuit) -> DAGCircuit:
        new_dag = DAGCircuit()  
        for qreg in dag.qregs.values():
            new_dag.add_qreg(qreg)
        for creg in dag.cregs.values():
            new_dag.add_creg(creg)

        skip_nodes = set()

        for node in dag.topological_op_nodes():
            if node in skip_nodes:
                continue

            if node.op.name == 'gpi2' and node.op.params == [0.5]:  # GPI2(pi)
                successors = [succ for succ in dag.quantum_successors(node) if isinstance(succ, DAGOpNode)]
                for next_node in successors:
                    if next_node.op.name == 'ms' and next_node.op.params == [0, 0, 0.25] and node.qargs[0] in next_node.qargs:
                        #print(f"Commuting gpi2 and ms nodes: {node} and {next_node}")
                      
                        new_dag.apply_operation_back(next_node.op, next_node.qargs, next_node.cargs)
                        new_dag.apply_operation_back(node.op, node.qargs, node.cargs)
                        skip_nodes.add(next_node)
                        break
                else:
                    # if no valid successor found, add the current operation to the new DAG
                    new_dag.apply_operation_back(node.op, node.qargs, node.cargs)
            else:
                new_dag.apply_operation_back(node.op, node.qargs, node.cargs)

        return new_dag