.PHONY: all test mut serve move mutmut

all: test mutmut

test:
	sh ./scripts/unit_test.sh

mutmut: mut move

mut:
	sh ./scripts/mutation_test.sh

move:
	sh ./scripts/move_mut.sh

serve:
	sh ./scripts/serve.sh