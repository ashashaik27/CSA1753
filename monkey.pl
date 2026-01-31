state(at_door,on_floor,at_window,has_not).
move(state(at_door,on_floor,X,has_not),
     walk,
     state(at_window,on_floor,X,has_not)).

move(state(at_window,on_floor,at_window,has_not),
     climb,
     state(at_window,on_box,at_window,has_not)).

move(state(at_window,on_box,at_window,has_not),
     grasp,
     state(at_window,on_box,at_window,has)).
