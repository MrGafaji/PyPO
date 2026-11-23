<script lang="ts">
  let reflectorsOpen = $state(true)
</script>

<svelte:head>
  <title>PyPO Workspace</title>
</svelte:head>

<div class="workspace">
  <aside class="element-pane" aria-label="Element palette">
    <h1>Elements</h1>

    <section class="accordion">
      <button
        class="accordion-trigger"
        aria-expanded={reflectorsOpen}
        aria-controls="reflector-elements"
        onclick={() => (reflectorsOpen = !reflectorsOpen)}
      >
        <svg
          class:collapsed={!reflectorsOpen}
          class="chevron"
          viewBox="0 0 16 16"
          fill="none"
          aria-hidden="true"
        >
          <path d="m4 6 4 4 4-4" stroke="currentColor" stroke-width="1.5" />
        </svg>
        <span class="accordion-label">Reflectors</span>
        <span class="item-count">1</span>
      </button>

      <div id="reflector-elements" class="accordion-content" role="list" hidden={!reflectorsOpen}>
        <div class="element-widget" role="listitem">
          <span class="element-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none">
              <path d="M7 3c7 3 7 15 0 18" stroke="currentColor" stroke-width="1.6" />
              <path d="M9 5 18 2M10.5 8.5 20 7M11 12h10M10.5 15.5 20 17M9 19l9 3" stroke="currentColor" stroke-width="1.2" />
            </svg>
          </span>
          <span class="element-name">Parabolic reflector</span>
        </div>
      </div>
    </section>
  </aside>

  <main class="workspace-canvas" aria-label="Empty workspace"></main>
</div>
