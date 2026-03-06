class QualityAgent:
    def handle_query(self, query):
        if "defect" in query.lower() or "rejection" in query.lower():
            return "ESCALATE"
        else:
            return "Quality check confirmed: Fabric meets standard specifications"

class ProductionAgent:
    def __init__(self):
        self.efficiency_record = {}

    def update_efficiency(self, loom_id, percentage):
        self.efficiency_record[loom_id] = percentage

    def check_status(self, loom_id):
        efficiency = self.efficiency_record.get(loom_id, 100)
        if efficiency < 50:
            return "ESCALATE"
        elif efficiency < 75:
            return "Warning: Loom efficiency below 75%"
        else:
            return "Production speed is optimal"

class FloorManagerAgent:
    def handle_issue(self, issue):
        print("\n{Floor Manager Agent is activated}")
        print("Issue received:", issue)
        if issue == "Critical Production Drop":
            print("Manager escalating to Plant Head...")
            return "ESCALATE_TO_HEAD"
        elif issue == "Quality Dispute Escalation":
            print("Manager reviewing batch quality reports...")
            return "ESCALATE_HEAD"
        else:
            print("Floor Manager resolved the operational issue")
            return "RESOLVED"

class PlantHeadAgent:
    def intervene(self, issue):
        print("\n{Plant Head intervention required}")
        print("Head resolving issue:", issue)
        print("Head has authorized maintenance/re-processing\n")

def main():
    print("===================")
    print("=== Textile Mill Multi-Agent System ===")
    print("===================")

    quality_agent = QualityAgent()
    production_agent = ProductionAgent()
    manager = FloorManagerAgent()
    head = PlantHeadAgent()

    print("\n -- Quality Inspection Section --")
    query = input("Enter quality query/report: ")
    response = quality_agent.handle_query(query)

    if response == "ESCALATE":
        mgr_response = manager.handle_issue("Quality Dispute Escalation")
        if mgr_response == "ESCALATE_HEAD":
            head.intervene("Major Fabric Defect Report")
    else:
        print("Quality Agent Response:", response)

    print("\n -- Production Efficiency Section --")
    loom_id = input("Enter Loom ID: ")
    efficiency = float(input("Enter efficiency percentage: "))
    production_agent.update_efficiency(loom_id, efficiency)
    status = production_agent.check_status(loom_id)

    if status == "ESCALATE":
        mgr_response = manager.handle_issue("Critical Production Drop")
        if mgr_response == "ESCALATE_TO_HEAD":
            head.intervene("Critical Loom Failure at " + loom_id)
    else:
        print("Production Status:", status)

    print("\n=== System processing complete ===")

if __name__ == "__main__":
    main()


# Fabric looks good, no issues
# Major defect found in the latest silk batch
# Loom-B2