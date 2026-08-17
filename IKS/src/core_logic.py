from dataclasses import dataclass
from typing import Iterable, Optional


# A Fact is represented as:
# (subject, property)
Fact = tuple[str, str]

# A Rule is represented as:
# (antecedent, consequent)
Rule = tuple[str, str]


def _validate_text(value: str, name: str) -> str:
    """Validate and clean a text value."""

    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string.")

    value = value.strip()

    if not value:
        raise ValueError(f"{name} cannot be empty.")

    return value


def validate_fact(fact: Fact) -> Fact:
    """Validate a fact represented as (subject, property)."""

    if not isinstance(fact, tuple) or len(fact) != 2:
        raise TypeError(
            "A fact must be a 2-item tuple: "
            "(subject, property)."
        )

    subject = _validate_text(fact[0], "Subject")
    property_name = _validate_text(fact[1], "Property")

    return subject, property_name


def validate_rule(rule: Rule) -> Rule:
    """Validate a rule represented as (antecedent, consequent)."""

    if not isinstance(rule, tuple) or len(rule) != 2:
        raise TypeError(
            "A rule must be a 2-item tuple: "
            "(antecedent, consequent)."
        )

    antecedent = _validate_text(rule[0], "Antecedent")
    consequent = _validate_text(rule[1], "Consequent")

    if antecedent == consequent:
        raise ValueError(
            "Antecedent and consequent must be different."
        )

    return antecedent, consequent


@dataclass(frozen=True)
class Proof:
    """Stores the five components of the generated explanation."""

    pratijna: str
    hetu: str
    udaharana: str
    upanaya: str
    nigamana: str


class InferenceEngine:
    """
    Rule-based inference engine inspired by
    the structure of Nyaya inference.
    """

    def __init__(
        self,
        facts: Optional[Iterable[Fact]] = None,
        rules: Optional[Iterable[Rule]] = None,
    ):
        self.facts: set[Fact] = set()
        self.rules: set[Rule] = set()

        # Add initial facts
        if facts:
            for fact in facts:
                subject, property_name = validate_fact(fact)
                self.add_fact(subject, property_name)

        # Add initial rules
        if rules:
            for rule in rules:
                antecedent, consequent = validate_rule(rule)
                self.add_rule(antecedent, consequent)

    def add_fact(
        self,
        subject: str,
        property_name: str
    ) -> None:
        """Add a fact to the knowledge base."""

        subject = _validate_text(subject, "Subject")
        property_name = _validate_text(
            property_name,
            "Property"
        )

        self.facts.add(
            (subject, property_name)
        )

    def add_rule(
        self,
        antecedent: str,
        consequent: str
    ) -> None:
        """Add a general inference rule."""

        antecedent, consequent = validate_rule(
            (antecedent, consequent)
        )

        self.rules.add(
            (antecedent, consequent)
        )

    def infer_all(self) -> set[Fact]:
        """
        Apply rules repeatedly until no new facts
        can be derived.

        This is the forward-chaining algorithm.
        """

        # Start with the original facts
        closure = set(self.facts)

        changed = True

        while changed:
            changed = False

            for antecedent, consequent in self.rules:

                # Make a copy of the current facts
                # so new facts can safely be added.
                current_facts = list(closure)

                for subject, property_name in current_facts:

                    # Check whether the rule can be applied
                    if property_name == antecedent:

                        new_fact = (
                            subject,
                            consequent
                        )

                        # Add only if it is a new fact
                        if new_fact not in closure:
                            closure.add(new_fact)
                            changed = True

        return closure

    def infer(self, query: Fact) -> bool:
        """Return True if the query can be inferred."""

        query = validate_fact(query)

        derived_facts = self.infer_all()

        return query in derived_facts

    def explain(
        self,
        query: Fact
    ) -> Optional[Proof]:
        """
        Generate a five-member explanation
        for an inferred query.
        """

        subject, conclusion = validate_fact(query)

        # Generate all possible facts
        derived_facts = self.infer_all()

        # If the query cannot be derived,
        # no explanation is generated.
        if (subject, conclusion) not in derived_facts:
            return None

        # Look for a rule that directly supports
        # the conclusion.
        for antecedent, consequent in self.rules:

            if consequent == conclusion:

                supporting_fact = (
                    subject,
                    antecedent
                )

                if supporting_fact in derived_facts:

                    return Proof(
                        pratijna=(
                            f"{subject} has "
                            f"{conclusion}."
                        ),

                        hetu=(
                            f"Because {subject} has "
                            f"{antecedent}."
                        ),

                        udaharana=(
                            f"Wherever something has "
                            f"{antecedent}, it has "
                            f"{conclusion}."
                        ),

                        upanaya=(
                            f"{subject} has "
                            f"{antecedent}, "
                            f"so the rule applies."
                        ),

                        nigamana=(
                            f"Therefore, {subject} has "
                            f"{conclusion}."
                        ),
                    )

        # If the query was already a given fact
        return Proof(
            pratijna=(
                f"{subject} has {conclusion}."
            ),

            hetu=(
                "The queried fact is already given."
            ),

            udaharana=(
                "No additional universal rule "
                "is required."
            ),

            upanaya=(
                f"{subject} directly has "
                f"{conclusion}."
            ),

            nigamana=(
                f"Therefore, {subject} has "
                f"{conclusion}."
            ),
        )