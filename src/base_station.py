import time
import json
import os

class BaseStation:
    """
    Görev Kontrol Merkezi (Base Station).
    Uç düğümlerden gelen verileri toplar, analiz eder ve nihai görev raporunu oluşturur.
    """
    def __init__(self):
        self.received_messages = []
        self.mission_start_time = time.time()
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")

    def receive_telemetry(self, node_id, data):
        """
        Uç düğümden telemetri/bulgu paketini alır.
        İletişim gecikmesi simüle edilebilir.
        """
        print(f"[BaseStation] {node_id} düğümünden paket alındı. İnceleme başlatılıyor...")
        
        message = {
            "arrival_time": time.time(),
            "node_id": node_id,
            "data": data
        }
        self.received_messages.append(message)
        
        if data.get("is_positive"):
            print(f"[BaseStation] !!! DİKKAT !!! {node_id} tarafından ONAYLANMIŞ biyolojik imza rapor edildi!")

    def generate_mission_report(self):
        """
        Tüm görev sürecini özetleyen kapsamlı bir rapor oluşturur.
        """
        total_events = len(self.received_messages)
        positives = [m for m in self.received_messages if m["data"].get("is_positive")]
        
        report = {
            "mission_duration": time.time() - self.mission_start_time,
            "total_nodes_reporting": len(set(m["node_id"] for m in self.received_messages)),
            "total_data_packets": total_events,
            "confirmed_biosignatures": len(positives),
            "summary": "Görev başarıyla tamamlandı." if total_events > 0 else "Veri alınamadı.",
            "detailed_findings": [m["data"] for m in positives]
        }

        # Raporu dosyaya kaydet
        report_path = os.path.join(self.output_dir, f"mission_report_{int(time.time())}.json")
        try:
            with open(report_path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=4, ensure_ascii=False)
            print(f"\n[BaseStation] Kapsamlı Görev Raporu oluşturuldu: {report_path}")
        except Exception as e:
            print(f"[BaseStation] Rapor kaydedilemedi: {e}")

        return report

    def display_dashboard(self):
        """
        Terminal üzerinde basit bir gösterge paneli sunar.
        """
        print("\n" + "="*50)
        print("      ASTROBIO EDGE - GÖREV KONTROL MERKEZİ")
        print("="*50)
        print(f"Alınan Paket Sayısı: {len(self.received_messages)}")
        print(f"Pozitif Bulgular   : {len([m for m in self.received_messages if m['data'].get('is_positive')])}")
        print("-" * 50)
        
        if self.received_messages:
            last_msg = self.received_messages[-1]
            print(f"Son Gelen Düğüm    : {last_msg['node_id']}")
            print(f"Son Sağlık Durumu : {last_msg['data'].get('health', 'BİLİNMİYOR')}")
            print(f"Son Batarya Seviyesi: {last_msg['data'].get('battery', '---')}")
        print("="*50 + "\n")
