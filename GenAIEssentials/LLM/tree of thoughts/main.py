import openai
import os

openai.api_key = "your-api-key"  # or use os.environ["OPENAI_API_KEY"]

def call_gpt(prompt):
    response = openai.responses.create(
        model="gpt-4",
        messages=prompt
    )
    return response.choices[0].message['content'].strip()

def generate_thoughts(state, n=3):
    prompt = f"Given the current idea: '{state}', suggest {n} next steps or thoughts."
    thoughts = call_gpt(prompt).split('\n')
    return [t.strip('- ') for t in thoughts if t.strip()]

def evaluate_state(state):
    prompt = f"Evaluate the following idea for solving the problem: '{state}'. Rate it from 1 to 10."
    score = call_gpt(prompt)
    try:
        return int([s for s in score.split() if s.isdigit()][0])
    except:
        return 0

def tree_of_thought_solver(initial_prompt, max_steps=3, beam_width=3):
    states = [initial_prompt]

    for step in range(max_steps):
        all_candidates = []
        for state in states:
            thoughts = generate_thoughts(state, n=beam_width)
            for thought in thoughts:
                new_state = state + ' -> ' + thought
                score = evaluate_state(new_state)
                all_candidates.append((new_state, score))
        
        # Keep top `beam_width` states
        all_candidates.sort(key=lambda x: x[1], reverse=True)
        states = [x[0] for x in all_candidates[:beam_width]]
    
    return states[0]  # Return best final state

# 🧪 Example usage
problem = "Write about some habits for coding."
final_solution = tree_of_thought_solver(problem)
print("\nBest Solution:\n", final_solution)
