"""Active blind-review candidates; retired sources live in archive/."""

def finding(id, claim, evidence, proof, tags):
    return dict(id=id, claim=claim, evidence=evidence, proof=proof, tags=tags)


SEARCH_FILTER=True

def build():
    from case_dacia import build as dacia
    return [dacia(search_filter=SEARCH_FILTER)]
