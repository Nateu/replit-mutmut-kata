.PHONY: test mut serve

test:
	sh ./scripts/unit_test.sh

mut:
	sh ./scripts/mutation_test.sh

serve:
	sh ./scripts/serve.sh