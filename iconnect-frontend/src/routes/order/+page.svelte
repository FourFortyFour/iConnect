<script>
  import { enhance } from "$app/forms";
</script>

<div class="content">
  <aside />
  <main class="order-form">
    <h2>Place Your Order</h2>
    <form action="?/pay" method="post" use:enhance>
      <label>
        Name:
        <input name="name" autocomplete="off" />
      </label>
      <button>Pay</button>
    </form>
  </main>
  <aside />
</div>

<style>
  .content {
    display: flex;
  }
  .order-form {
    flex: 3;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    background-color: gainsboro;
  }
  aside {
    flex: 1;
  }
</style>
