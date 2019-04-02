import React from "react";
import { Route, Switch } from "react-router-dom";
import Body from "./components/Body";
import NotFound from "./components/NotFound";
import Login from "./components/Login";
import Signup from "./components/Signup";



export default () =>
  <Switch>
    <Route path="/" exact component={Body} />
    <Route path="/login" exact component={Login} />
    <Route path="/signup" exact component={Signup} />
    { /* Finally, catch all unmatched routes */ }
    <Route component={NotFound} />

  </Switch>;
