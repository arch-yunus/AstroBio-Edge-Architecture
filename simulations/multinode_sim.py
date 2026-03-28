import sys
import os
import time

# Adding project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.mesh_coordinator import MeshCoordinator
from src.utils.data_logger import DataLogger

def run_mission():
    print("STARTING: AstroBio-Edge Multi-Node Mission Simulation")
    print("-------------------------------------------------------")
    
    logger = DataLogger()
    coordinator = MeshCoordinator(swarm_size=3)
    
    # Simulate a 2-cycle scan mission
    coordinator.orchestrate_swarm(cycles=2)
    
    # Log the final results
    print("\n[Simulator] Finalizing mission logs...")
    for event in coordinator.global_registry:
        logger.log_event(event)
        
    print("\n[Simulator] Mission Complete. Check logs/ directory for results.")

if __name__ == "__main__":
    run_mission()
