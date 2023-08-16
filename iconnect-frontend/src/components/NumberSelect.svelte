<script>
  export let name;
  export let price;

  const baseVal = $price;
  let value = 1;
</script>

<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
/>

<div class="number-selector">
  <input
    {name}
    class="val"
    type="number"
    bind:value
    on:change={() => {
      if (value >= 1) {
        price.set(baseVal * value);
      } else {
        value = 1;
        price.set(baseVal * value);
      }
    }}
    required
    min="1"
  />
  <div class="btns">
    <span
      class="icn material-symbols-outlined"
      on:click={() => {
        if (value !== 1) {
          value--;
          price.set(baseVal * value);
        }
      }}
    >
      chevron_left
    </span>
    <span
      class="icn material-symbols-outlined"
      on:click={() => {
        value++;
        price.set(baseVal * value);
      }}
    >
      chevron_right
    </span>
  </div>
</div>

<style>
  .val {
    border: none;
    background-color: rgb(244, 244, 244);
    width: 3vw;
    text-align: center;
    font-size: 18px;
  }

  .val:focus {
    outline: none;
    border-bottom: 2px solid black;
  }

  .val::-webkit-inner-spin-button,
  .val::-webkit-outer-spin-button {
    display: none;
  }
  .number-selector {
    display: flex;
  }

  .icn {
    height: 100%;
    cursor: pointer;
    user-select: none;
  }

  .icn:hover {
    background-color: rgb(244, 244, 244);
  }
</style>
