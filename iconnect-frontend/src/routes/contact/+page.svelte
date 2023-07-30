<main>
  <h1>CONTACT</h1>
  <section>
    <form action="" method="post">
      <label for="name">
        <input type="text" name="name" placeholder="John doe" />
      </label>
      <label for="email">
        <input
          type="email"
          name="email"
          placeholder="email@mail.com"
          required
        />
      </label>
      <label for="msg">
        <textarea
          name="msg"
          id=""
          cols="30"
          rows="10"
          placeholder="Message"
          required
        />
      </label>
      <button>Send</button>
    </form>
    <p>Placeholder image</p>
  </section>
</main>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    margin: 0px;
    font-family: "Cabin Condensed", sans-serif;
  }
  h1 {
    margin: 2% 0%;
  }
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  section {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: 100%;
  }

  section > * {
    padding: 2%;
  }
  form {
    display: flex;
    flex-direction: column;
    flex: 1;
    align-items: center;
  }

  p {
    flex: 1;
    display: flex;
    justify-content: center;
  }

  label {
    width: 70%;
    margin-bottom: 2%;
  }

  input {
    font-size: 18px;
    border-radius: 25px;
    width: 100%;
    border: 0.05px solid black;
    padding: 2%;
  }

  textarea {
    font-size: 18px;
    border-radius: 25px;
    width: 100%;
    border: 0.05px solid black;
    padding: 2%;
  }
  button {
    background-color: black;
    color: white;
    border: none;
    font-size: 16px;
    padding: 2% 6%;
    border-radius: 25px;
  }
</style>
