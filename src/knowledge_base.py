from pathlib import Path


DOC_KEYWORDS = {
    "certification_requirements.md": [
        "certification",
        "certified",
        "missing certification",
        "pending certification",
    ],
    "audit_frequency_rules.md": [
        "audit",
        "outdated audit",
        "last audit",
        "12-month",
    ],
    "risk_scoring_guide.md": [
        "risk",
        "score",
        "high risk",
        "medium risk",
        "low risk",
        "threshold",
    ],
    "corrective_action_playbook.md": [
        "action",
        "follow-up",
        "corrective",
        "water",
        "waste",
        "labor",
        "emissions",
    ],
    "supplier_esg_policy.md": [
        "esg",
        "supplier",
        "sustainability",
        "review",
        "policy",
    ],
}


def load_knowledge_documents(docs_path):
    """Load markdown knowledge-base documents from the docs folder."""
    documents = {}

    for file_path in docs_path.glob("*.md"):
        documents[file_path.name] = file_path.read_text(encoding="utf-8")

    return documents


def select_relevant_documents(reasoning_items, documents):
    """
    Select relevant knowledge documents based on the reasoning generated
    by the supplier risk scoring logic.
    """
    combined_reasoning = " ".join(reasoning_items).lower()
    selected = []

    for document_name, keywords in DOC_KEYWORDS.items():
        if document_name not in documents:
            continue

        for keyword in keywords:
            if keyword.lower() in combined_reasoning:
                selected.append(document_name)
                break

    if not selected:
        selected.append("supplier_esg_policy.md")
        selected.append("risk_scoring_guide.md")

    return selected


def create_grounding_summary(selected_documents, documents):
    """
    Create a short grounding summary using the first meaningful paragraph
    from each selected document.
    """
    grounding_items = []

    for document_name in selected_documents:
        document_text = documents.get(document_name, "")
        paragraphs = [
            paragraph.strip()
            for paragraph in document_text.split("\n\n")
            if paragraph.strip() and not paragraph.strip().startswith("#")
        ]

        if paragraphs:
            grounding_items.append(
                {
                    "source": document_name,
                    "excerpt": paragraphs[0],
                }
            )

    return grounding_items


def get_grounding_for_supplier(reasoning_items):
    """
    Retrieve relevant local policy guidance for a supplier risk result.

    This local retrieval scaffold is designed to mirror the type of
    grounded knowledge retrieval that will later be implemented with Foundry IQ.
    """
    project_root = Path(__file__).resolve().parents[1]
    docs_path = project_root / "docs"

    documents = load_knowledge_documents(docs_path)
    selected_documents = select_relevant_documents(reasoning_items, documents)

    return create_grounding_summary(selected_documents, documents)