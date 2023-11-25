#!/bin/bash -x

declare -a branches=(
  "RAG"
  "adding-a-field"
  "adding-an-optional-field"
  "chitchat"
  "clarification"
  "corrections"
  "flow-guards"
  "linking-flows"
  "main"
  "new-flow"
  "nlu-triggers"
  "pattern_cancel_flow"
  "pattern_continue_interrupted"
  "rephrasing"
  "slot-validation"
)

for branch in "${branches[@]}"
do
  git checkout $branch
  rasa train
  git checkout -- config.yml
  rasa run actions &
  ACTION_SERVER_PID=$!
  rasa test e2e e2e_tests
  kill $ACTION_SERVER_PID
done

git checkout main
