const { Plugin } = require('obsidian');
const { layer, RectangleMarker } = require('@codemirror/view');

// Draw only the primary insertion caret. Obsidian still owns text selections,
// secondary cursors, input, and IME. No global document or window coordinates.
module.exports = class BearCursor extends Plugin {
  onload() {
    this.registerEditorExtension(layer({
      above: true,
      class: 'bear-cursor-layer',
      markers(view) {
        const range = view.state.selection.main;
        if (!range.empty || view.composing || view.dom.classList.contains('cm-vimMode')) {
          return [];
        }
        const markers = RectangleMarker.forRange(view, 'bear-cursor-caret', range);
        const { node } = view.domAtPos(range.head);
        const element = node.nodeType === 1 ? node : node.parentElement;
        const line = element.closest('.cm-line');
        // CodeMirror measures the glyph box; the native caret fills the line.
        // Keep CodeMirror's position and extend equally above and below it.
        const lineHeight = line && parseFloat(view.dom.ownerDocument.defaultView
          .getComputedStyle(line).lineHeight) * view.scaleY;
        return markers.map(marker => {
          const height = Math.max(marker.height, lineHeight || 0);
          return new RectangleMarker('bear-cursor-caret', marker.left,
            marker.top - (height - marker.height) / 2, null, height);
        });
      },
      update(update, element) {
        if (update.selectionSet || update.docChanged || update.focusChanged) {
          element.style.animationName = element.style.animationName === 'bear-caret-blink'
            ? 'bear-caret-blink-alt' : 'bear-caret-blink';
        }
        return update.docChanged || update.selectionSet || update.focusChanged;
      }
    }));
  }
};
