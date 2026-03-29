import time
import os
import sys
import random

# Adding project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.mesh_coordinator import MeshCoordinator
from src.base_station import BaseStation
from src.utils.report_generator import generate_final_report
from src.utils.dashboard_manager import DashboardManager
from src.utils.data_logger import DataLogger

def run_astro_mission(swarm_size=4, cycles=5):
    """
    ASTROBIO-EDGE MİSYONU - v0.5.0 SOVEREIGNTY TIER
    Adaptif sürü zekası ve profesyonel görselleştirme ile.
    """
    # 1. Altyapıyı Hazırla
    base_station = BaseStation()
    coordinator = MeshCoordinator(swarm_size=swarm_size)
    dashboard = DashboardManager()
    logger = DataLogger()
    mission_logs = ["Misyon Kontrolü Başlatıldı", f"{swarm_size} otonom düğüm çevrimiçi"]
    
    # 2. Görev Döngülerini Başlat
    for cycle in range(cycles):
        mission_logs.append(f"Döngü {cycle+1} başlatılıyor...")
        
        # Rastgele Güneş Fırtınası Olasılığı (%15)
        solar_storm = random.random() < 0.15
        if solar_storm:
            mission_logs.append("! UYARI: Güneş Patlaması Tespit Edildi !")
        
        # Her düğüm için hata enjektörünü güncelle (Güneş fırtınası durumu)
        for node in coordinator.nodes:
            node.fault_injector.update_solar_storm_status(solar_storm)
            
            # Adaptif modda ise CPU yükünü artır
            cpu_usage = 0.8 if coordinator.adaptive_mode else 0.4
            
            # Düğümü çalıştır
            sun_exposure = (cycle % 2 == 0)
            event = node.run_discovery_cycle(sun_exposure=sun_exposure)
            
            # Verileme ve Loglama
            base_station.receive_telemetry(node.node_id, event)
            logger.log_event(event) # Kriptografik güvenli loglama
            
            if event["is_positive"]:
                mission_logs.append(f"!!! {node.node_id} bulgu raporladı!")

            # Dashboard Güncellemesi (Her düğümden sonra canlı)
            dashboard.render_mission(
                [n.logs[-1] if n.logs else {} for n in coordinator.nodes],
                coordinator.get_swarm_status(),
                mission_logs
            )
            time.sleep(0.4)
            
        # Döngü sonu koordinasyon (Adaptasyon ve Konsensüs)
        coordinator.orchestrate_swarm(cycles=0) # Sadece iç mantığı çalıştırmak için (0 cycles)
        time.sleep(1)

    # 3. Misyon Sonu Raporu
    mission_summary = base_station.generate_mission_report()
    generate_final_report(mission_summary)
    
    # Final Mesajı
    dashboard.console.print("\n[bold green]GÖREV BAŞARIYLA TAMAMLANDI. Tüm veriler mühürlendi ve merkezi sunucuya iletildi.[/bold green]")
    dashboard.console.print(f"Rapor Yolu: logs/mission_dashboard.html")

if __name__ == "__main__":
    size = 3
    steps = 4
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    if len(sys.argv) > 2:
        steps = int(sys.argv[2])
        
    try:
        run_astro_mission(swarm_size=size, cycles=steps)
    except KeyboardInterrupt:
        print("\n[!] Misyon kullanıcı tarafından durduruldu.")
