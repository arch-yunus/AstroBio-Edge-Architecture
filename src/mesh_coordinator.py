import sys
import os

# Adding project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.edge_node import EdgeNode

class MeshCoordinator:
    def __init__(self, swarm_size=3):
        self.nodes = [EdgeNode(node_id=f"Astro-Edge-{i+1:02d}") for i in range(swarm_size)]
        self.global_registry = []

    def orchestrate_swarm(self, cycles=1):
        print(f"[Coordinator] Orchestrating swarm of {len(self.nodes)} nodes...")
        
        for c in range(cycles):
            print(f"\n--- Mission Cycle {c+1} ---")
            cycle_results = []
            
            for node in self.nodes:
                event = node.run_discovery_cycle()
                cycle_results.append(event)
                self.global_registry.append(event)
            
            self.check_consensus(cycle_results)

    def check_consensus(self, results):
        """
        Quorum sensing: If > 50% nodes detect biosignature, trigger High-Priority Alert.
        """
        positives = [r for r in results if r['is_positive']]
        threshold = len(results) / 2
        
        if len(positives) > threshold:
            print(f"\n[Coordinator] QUORUM REACHED! Consensus on Biosignature detected at target site.")
            avg_confidence = sum(r['confidence'] for r in positives) / len(positives)
            print(f"[Coordinator] Aggregated Confidence: {avg_confidence:.2f}")
        elif len(positives) > 0:
            print(f"\n[Coordinator] Partial detection ({len(positives)}/{len(results)} nodes). Requesting ROI re-scan.")
        else:
            print(f"\n[Coordinator] Nominal telemetry across all nodes.")

if __name__ == "__main__":
    coordinator = MeshCoordinator(swarm_size=4)
    coordinator.orchestrate_swarm(cycles=2)
