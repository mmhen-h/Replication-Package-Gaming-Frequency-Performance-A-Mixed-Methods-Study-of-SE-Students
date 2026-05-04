## Step 2: Coding and Analysis

**Prompt 4**
- Next is Step 2: Coding and Analysis. Here are the instructions:
Use the Keyword Reference Map we provided below in the prompt to assign subcodes.

Exhaustive Coding: Extract every possible subcode found in a single response.

Row Duplication: If a response contains multiple subcodes, duplicate the row so each row in your output corresponds to exactly one subcode.

Markdown Highlighting: In the response column, bold only the keyword or a keyphrase(part of the sentence) that triggered that specific row's subcode.

- Example (keyword): If a response is "I value *cooperation* and *planning*," the row for CLB-COP should only bold cooperation, and the row for PRO-STR should only bold planning.

- Example(keyphrase): If a response is "Learning *to operate in teams to achieve some goal is the basis of teamwork*. This is used in any scenario in video games where teams are involved *regardless of voice chat, text chat, or any form of communication*,"CLB-MNG should only bold the phrase "to operate in teams to achieve some goal is the basis of teamwork", and the row for COM-EFF should only bold the phrase "regardless of voice chat, text chat, or any form of communication".



We have also attached a CSV named CODEDgaming25fa1.csv, where a human manually coded the responses as an example.


Keyword Reference Map (edited to include keywords and phrases from manually coded CSVs)

Assign subcodes based on these specific phrases:


Teamwork Competencies

Communication (COM)
COM-PSR (Under Pressure): pressure, stressful, stress, intense, high-pressure, heat of the moment, panic, clutch, tension, heated, high stakes, destroyed, fast-paced, stay calm under pressure, high-stress, tone, do not irritate or stress out other players

COM-EFF (Efficiency): efficiently, efficient, quick, concise, short, fast, brevity, streamlined, rapid, summarize, swiftly, unneeded information, effectively communicate, quickly, get rid of unneeded information, effective communication, communicate shortly, communicate information quickly, practice communication, effectively communicate, explaining thinking process, relaying stats, real time feedback

COM-CLR (Clarity): clearly, clarity, clear, communication clarity, direct, articulate, precise, understandable, specific, vocal, callouts, relaying information, precisely, express myself, expressive, necessary communication, clear communication, explain through a mic, articulate yourself, convey your ideas, use your words, communicative and clear, semantic information, proactive communicator

Collaboration (CLB)
CLB-COP (Cooperation): cooperation, cooperate, cooperating, collaborative, collaborate, collaboration, working together, harmony, synergy, unity, joint, unison, combine, coordinating, coordinate, work along side, cooperative, work together, lean on, work as a team, working as a team, value of teams, team efforts, coordination, cohesion, syncing strategies, sharing resources, team coordination, cooperate to do well, basis of teamwork, syncing strategies, social games

CLB-MNG (Task Management): skillsets, individual skills, strengths, allocate tasks, specialized roles, role, skills, abilities, capabilities, expertise, talent, utility, composition, comp, specialized, skill sets, divide and conquer, dividing and conquering, part you're good at, know your roles, fit into the team, play around your team, strengths and weaknesses, complement each other, individual strengths, specialized duties, specific roles, role for each player, understanding what roles to play, perfect combinations of action, operate in teams, play to teammates' strengths, gauge what everyone's skills are, roles based on dynamics, figure out what each person wants

CLB-DEL (Delegation): task delegation, delegation, delegate, assign tasks, assigning tasks, distributing tasks, hand off, tasking, give orders, taking orders, allocate tasks, divvy up tasks, delegate tasks

CLB-CMR (Comradery): comradery, camaraderie, group responsibility, team spirit, bond, friendship, morale, cohesion, trust, closeness, bonding, chemistry, stay engaged, having a good time, getting along well together, tool for collaboration, work together in a complete way, support system, voice heard, trust teammates

Problem Solving (PRO)
PRO-STR (Strategic Planning): strategy, strategize, strategizing, plan, planning, tactical, tactics, approach, methodology, prep, preparation, shotcalling, pre-game, strategic, risk to reward, positioning, optimal routes, solving problems, solve problems, weigh risk to reward, game plan, tactical planning, explain the process, optimize something, strategize how to win, approach objectives, think methodically, determine next steps, problem-solving from a different perspective

PRO-ADP (Adaptability): adaptability, adapt, adapting, changing course, flexible, shift, changing, adjust, adjusting, pivot, pivoting, versatility, situational, adapt to, adapting your play style, adjusting to skills of others, adapt to different roles, read team dynamics, adapt interactions

PRO-GOL (Goal Alignment): goal setting, goal, objective, aim, target, shared goal, primary goal, mission, win condition, purpose, common goal, complete goals, reach a desired goal, achieve goals, move the project forward

Interpersonal Skills (INT)
INT-GRP (Group Dynamics): working in a group, group, team player, teamwork, ensemble, collective, community, team environment, co-op, multiplayer, teams, good teammate, team projects, different types of people, dealing with individuals, team based games, benefits the group

INT-OTH (Putting Others First): put others first, help, support, assist, sacrifice, selfless, altruism, aid, healer, buffing, peeling, backing up, revive, helping others, look out for, backup, supporting others, help others thrive, making their job easier, help team rather than stats, step back and support, remain selfless, accommodating others

INT-ENC (Encouragement): encouragement, encourage, encouraging, positive, morale, uplift, cheer, motivating, motivation, kindness, reassuring, positive team energy, encourages positive team work, encourage each other, helps confidence, socially engaged, positive team work

INT-PAT (Patience): patience, patient, calm, composure, level-headed, tolerant, tolerance, waiting, not getting mad, tolerating, control of emotions, keep an even keel, even keel, patience as a skill

INT-PER (Perspective): understand others' perspectives, perspective, empathy, understand others, understanding others, views, standpoint, point of view, see their side, perspective flip, anticipate what others think, accept influence

INT-BND (Boundaries): boundaries, boundary, respect, limit, etiquette, manners, polite

INT-AWR (Team Awareness): team awareness, awareness, situational awareness, monitoring, tracking teammates, keeping tabs, map awareness, spatial awareness, listen to needs, aware of limitations, stop what I am working on to help others, assigned tasks, pay attention to teammates, observe opponents

INT-VUL (Vulnerability): vulnerability, vulnerable, mistakes, ownership, admitting, faults, learning from failure, wrong, aware of limitations, knowing when to ask for help, take failure in stride, thinking where I went wrong

Teamwork Barriers

Self-Efficacy (SEF)
SEF-DTR (Detriment): presence hurts, detriment, drag down, burden, handicap, weight, weaker, useless, bad at the game, holding the team back, drag the team down, detriments the team, results in discord

SEF-LCK (Lack of Faith): lack of faith, unsure, doubt, insecure, second-guess, low confidence, uncertain, scared, not confident, frustrated dealing with inadequacies

SEF-FLW (Follower): follower, follow, avoid blame, passive, back seat, listening to orders, do what I'm told, taking a back seat, let others lead

Defensive Isolation (DEF)
DEF-SLO (Solo Play): single-player, solo, avoid human interaction, alone, antisocial, isolation, single player, play by myself, solo games, only play games where you're alone

DEF-IRR (Irritation): irritation, irritated, mistakes, playstyles, annoyed, frustration, rage, mad, angry, bad teammates, getting annoyed, frustrated with others, uncooperative teammates, demanding others to do their play style

DEF-ISO (Negative Isolation): negative behavior, isolating, toxic, toxicity, harassment, griefing, flame, flaming, mean, rude, toxic environments, negative community, toxic pleasure, very negative teammate

Control & Disconnection (CTR)
CTR-DCT (Dictation): dictate, control, anxiety of losing, bossy, micromanage, micromanaging, telling people what to do, taking control, bossing people around, micromanage others, unilateral choices

CTR-LWF (Lone Wolf): lone wolf, disconnection, disconnected, rogue, independent, ignore team, doing my own thing, off on my own, work independently, solo player in a team, go off on my own

Devaluation (DEV)
DEV-NRL (Not Real Life): don't translate, real-life, real world, useless outside, stay in game, no external value, not applicable, doesn't help in the real world, only for games, specifically in video games, does not necessarily translate

DEV-VCM (Vacuum): vacuum, no external meaning, pointless, waste of time, meaningless, just a game, no real-world application, waste of effort, relief game

Please start with FA22_Cleaned_Data.csv

**Results of Prompt 4** 
