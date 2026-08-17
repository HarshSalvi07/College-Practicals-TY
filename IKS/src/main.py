from core_logic import InferenceEngine


def read_positive_integer(prompt: str) -> int:
    """Read a non-negative integer from the user."""

    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Please enter 0 or a positive integer.")
                continue

            return value

        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    print("=" * 60)
    print("NYAYA LOGIC AS AN INFERENCE ENGINE")
    print("=" * 60)

    # Create the inference engine
    engine = InferenceEngine()

    # --------------------------------------------------
    # Enter Facts
    # --------------------------------------------------

    fact_count = read_positive_integer(
        "\nEnter number of facts: "
    )

    for i in range(fact_count):

        print(f"\nFact {i + 1}")

        subject = input("Enter subject: ").strip()
        property_name = input("Enter property: ").strip()

        try:
            engine.add_fact(
                subject,
                property_name
            )

        except (TypeError, ValueError) as error:
            print(f"Invalid fact: {error}")
            return

    # --------------------------------------------------
    # Enter Rules
    # --------------------------------------------------

    rule_count = read_positive_integer(
        "\nEnter number of rules: "
    )

    for i in range(rule_count):

        print(f"\nRule {i + 1}")
        print("Example format: smoke -> fire")

        rule_input = input("Enter rule: ").strip()

        try:
            parts = rule_input.split("->")

            if len(parts) != 2:
                raise ValueError

            antecedent = parts[0].strip()
            consequent = parts[1].strip()

            engine.add_rule(
                antecedent,
                consequent
            )

        except ValueError:
            print(
                "Invalid rule. "
                "Use the format: antecedent -> consequent"
            )
            return

        except (TypeError, ValueError) as error:
            print(f"Invalid rule: {error}")
            return

    # --------------------------------------------------
    # Enter Query
    # --------------------------------------------------

    print("\nQuery")

    query_subject = input(
        "Enter query subject: "
    ).strip()

    query_property = input(
        "Enter query property: "
    ).strip()

    query = (
        query_subject,
        query_property
    )

    try:
        result = engine.infer(query)

    except (TypeError, ValueError) as error:
        print(f"Invalid query: {error}")
        return

    # --------------------------------------------------
    # Display Inference Result
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("INFERENCE RESULT")
    print("=" * 60)

    if result:

        print("TRUE - The query can be inferred.")

        proof = engine.explain(query)

        if proof:

            print("\nFive-Member Explanation")
            print("------------------------")

            print(
                f"1. Pratijna   : "
                f"{proof.pratijna}"
            )

            print(
                f"2. Hetu       : "
                f"{proof.hetu}"
            )

            print(
                f"3. Udaharana  : "
                f"{proof.udaharana}"
            )

            print(
                f"4. Upanaya    : "
                f"{proof.upanaya}"
            )

            print(
                f"5. Nigamana   : "
                f"{proof.nigamana}"
            )

    else:

        print(
            "FALSE - The query cannot be inferred."
        )

    # --------------------------------------------------
    # Display Derived Facts
    # --------------------------------------------------

    derived_facts = engine.infer_all()

    print("\nDerived Knowledge")
    print("-----------------")

    for subject, property_name in sorted(
        derived_facts
    ):
        print(
            f"- {subject} has {property_name}"
        )


if __name__ == "__main__":
    main()