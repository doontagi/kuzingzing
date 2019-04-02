import React from "react";
// import axios from "axios";
import Form from "./Form";
import Posts from "./Posts";

export default class Body extends React.Component {
  state = {
    posts: []
  };

  // async componentDidMount() {
  //   const users = await axios.get("https://jsonplaceholder.typicode.com/users");
  //   console.log(users.data);
  // }

  handleAddPost = post => {
    if (post) {
      this.setState(prevState => ({
        posts: prevState.posts.concat(post)
      }));
    }
  };

  handleUpVote = timestamp => {
    const newPosts = this.state.posts.slice();
    for (let post of newPosts) {
      if (post.timestamp === timestamp) {
        post.score = post.score + 1;
      }
    }
    this.setState(() => ({
      posts: newPosts
    }));
  };

  handleDownVote = timestamp => {
    const newPosts = this.state.posts.slice();
    for (let post of newPosts) {
      if (post.timestamp === timestamp) {
        post.score = post.score - 1;
      }
    }
    this.setState(() => ({
      posts: newPosts
    }));
  };

  render() {
    return (
      <div>
        <main>
          <Form handleAddPost={this.handleAddPost} />
          <Posts
            posts={this.state.posts}
            handleUpVote={this.handleUpVote}
            handleDownVote={this.handleDownVote}
          />
        </main>
      </div>
    );
  }
}
