#!/bin/bash -xe

declare -a branches=(
  "RAG"
  "adding-a-field"
  "adding-an-optional-field"
  "chitchat"
  "clarification"
  "corrections"
  "flow-guards"
  "linking-flows"
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
  git rebase main
  git push -f origin $branch
done

git checkout main
