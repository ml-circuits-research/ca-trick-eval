"""Active adversarial candidate. Rejected and abandoned trials live in archive/."""
def finding(id, claim, evidence, proof, tags):
    return dict(id=id, claim=claim, evidence=evidence, proof=proof, tags=tags)

def build():
    from case_policy import build as policy
    from case_criogena import build as criogena
    return [policy(),criogena()]
