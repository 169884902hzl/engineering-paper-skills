**Draft With Placeholders**

Prior work addresses parts of this problem along several technical axes. Active perception methods treat viewpoint selection as part of manipulation, moving the camera or choosing a more informative view before action execution [citation needed: active perception or view selection for manipulation]. Visual servoing and guarded insertion methods instead emphasize feedback during execution, using online visual or contact information after an insertion action has been selected [citation needed: visual servoing for manipulation; citation needed: guarded insertion]. Language- and VLM-guided manipulation broadens target and action proposal from semantic task descriptions [citation needed: VLM or language-guided manipulation], but this line is distinct from jointly selecting an exact insertion pose, requesting additional visual evidence before contact, and handing the result to a guarded insertion controller. Multi-view manipulation is the closest comparison axis because it connects additional observations to downstream action selection [citation needed: multi-view manipulation]. The setting considered here focuses on partial occlusion near contact: when pose confidence is insufficient, the system requests an extra view before committing to guarded insertion.

**Citation Scaffold**

| Axis | Placeholder | Must Support |
|---|---|---|
| Active perception | `[citation needed: active perception/view selection for manipulation]` | Camera motion or view choice before action |
| Visual servo / guarded insertion | `[citation needed: visual servoing or guarded insertion]` | Feedback during execution, especially insertion |
| VLM manipulation | `[citation needed: language/VLM-guided manipulation]` | Semantic target or action proposal |
| Multi-view manipulation | `[citation needed: multi-view manipulation]` | Extra observations tied to action selection |