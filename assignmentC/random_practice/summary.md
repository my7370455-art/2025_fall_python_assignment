in this markdown, we need to document the inspiration from those practices.

choose_the_player:
the transfer equation is fairly reasonable, but it's hard to generate. Just remember in the future if you are given multiple choice in one dp problem regarding i, then maybe your dp table should contain more than one number for each i.
boredom:
i learned Counter, which is capable of quickly counting the appearing time of certain element. It's all about downsize the huge sequence-noticing what we need to solve has nothing to do with order.
maze_easiest:
we can store step and visit state in one matrix. this is super easy, making it no need to track steps in queue. by the way, deque is a good tool when solving those queue or stack questions.
number_operation:
in this problem, we can also store steps and visit state in one long list. the most important thing is to realize it's a bfs question. to think reversely, storing steps in queue is also reasonable in maze.
vacation:
setting the first case for dp table is also important. must do it right lol. dp table too.
wealthy_ppl:
i cannot find the solution by myself. it adopts a similar method to kadane but... the discard one strategy is tricky. somehow i feel it's like differenciation equation in math, it's harder to generate it than guessing it.
pots:
i suddenly wonder how openjudge identify presentation error. meanwhile, this program can still be optimized, if i redesign visited, however i don't know how to achieve this. i mean, store integer in visited.
