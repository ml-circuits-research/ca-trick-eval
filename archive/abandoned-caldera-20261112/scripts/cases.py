"""Active blind-review candidates; retired sources live in archive/."""

def finding(id, claim, evidence, proof, tags):
    return dict(id=id, claim=claim, evidence=evidence, proof=proof, tags=tags)



def build():
    from case_caldera import build as caldera
    return [caldera()]
