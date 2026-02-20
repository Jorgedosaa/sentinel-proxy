from presidio_analyzer import AnalyzerEngine

class SentinelScanner:
    def __init__(self):
        self.analyzer = AnalyzerEngine()

    def scan_text(self, text: str) -> list:
        """
        Scans input text for sensitive PII entities.
        """
        results = self.analyzer.analyze(
            text=text, 
            entities=[], 
            language='en'
        )
        
        
        findings = [
            {
                "entity_type": res.entity_type,
                "confidence": res.score,
                "start": res.start,
                "end": res.end
            }
            for res in results
        ]
            
        return findings

scanner = SentinelScanner()