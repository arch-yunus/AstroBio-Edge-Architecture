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
        print(f"[Koordinatör] {len(self.nodes)} düğümlük sürü yönetiliyor...")
        
        for c in range(cycles):
            print(f"\n--- Görev Döngüsü {c+1} ---")
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
            print(f"\n[Koordinatör] KORUM SAĞLANDI! Hedef bölgede Biyolojik İmza üzerinde konsensüs sağlandı.")
            avg_confidence = sum(r['confidence'] for r in positives) / len(positives)
            print(f"[Koordinatör] Birleşik Güven Oranı: {avg_confidence:.2f}")
        elif len(positives) > 0:
            print(f"\n[Koordinatör] Kısmi tespit ({len(positives)}/{len(results)} düğüm). Bölgenin yeniden taranması isteniyor.")
        else:
            print(f"\n[Koordinatör] Tüm düğümlerde nominal telemetri.")

if __name__ == "__main__":
    coordinator = MeshCoordinator(swarm_size=4)
    coordinator.orchestrate_swarm(cycles=2)
