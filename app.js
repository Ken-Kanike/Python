/**
 * Python Master Playground - Interactive Application Logic
 * Supports Pyodide WASM execution, VFS synchronization, dynamic file exploration,
 * syntax highlighting, search & categorization, and interactive REPL.
 */

(function () {
  'use strict';

  // --- Application State ---
  const state = {
    catalog: [],
    activeFile: null,
    modifiedFiles: new Map(), // path -> modified content string
    activeCategory: 'all',
    searchQuery: '',
    pyodide: null,
    isPyodideLoading: true,
    isExecuting: false,
    replHistory: [],
    replHistoryIndex: -1,
  };

  // --- DOM Elements ---
  const elements = {
    runtimeBadge: document.getElementById('runtime-status-badge'),
    runtimeText: document.getElementById('runtime-status-text'),
    searchInput: document.getElementById('file-search-input'),
    btnClearSearch: document.getElementById('btn-clear-search'),
    categoryChips: document.querySelectorAll('.category-filter-chips .chip'),
    fileTreeContainer: document.getElementById('file-tree-container'),
    fileCounterLabel: document.getElementById('file-counter-label'),
    btnRefreshCatalog: document.getElementById('btn-refresh-catalog'),

    activeFileTitle: document.getElementById('active-file-title'),
    modifiedIndicator: document.getElementById('modified-indicator'),
    btnResetCode: document.getElementById('btn-reset-code'),
    btnCopyCode: document.getElementById('btn-copy-code'),
    btnDownloadCode: document.getElementById('btn-download-code'),
    btnRunCode: document.getElementById('btn-run-code'),
    runButtonText: document.getElementById('run-button-text'),

    codeTextarea: document.getElementById('code-editor-textarea'),
    lineNumbers: document.getElementById('line-numbers'),

    terminalBody: document.getElementById('terminal-body'),
    executionTimeBadge: document.getElementById('execution-time-badge'),
    btnToggleRepl: document.getElementById('btn-toggle-repl'),
    btnClearTerminal: document.getElementById('btn-clear-terminal'),
    replBar: document.getElementById('terminal-repl-bar'),
    replInput: document.getElementById('repl-input'),
    btnSubmitRepl: document.getElementById('btn-submit-repl'),

    btnCopyClone: document.getElementById('btn-copy-clone'),
    toast: document.getElementById('toast'),
  };

  // --- Utility: Toast Notification ---
  let toastTimer = null;
  function showToast(message, duration = 3000) {
    if (!elements.toast) return;
    elements.toast.textContent = message;
    elements.toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      elements.toast.classList.remove('show');
    }, duration);
  }

  // --- Utility: Escape HTML ---
  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // --- Catalog Loader ---
  async function loadCatalog() {
    try {
      if (window.CODE_CATALOG && Array.isArray(window.CODE_CATALOG) && window.CODE_CATALOG.length > 0) {
        state.catalog = window.CODE_CATALOG;
      } else {
        const response = await fetch('code_catalog.json');
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        state.catalog = await response.json();
      }
    } catch (err) {
      console.warn('Could not load code_catalog.json directly:', err);
      if (window.CODE_CATALOG) {
        state.catalog = window.CODE_CATALOG;
      }
    }

    if (!state.catalog || state.catalog.length === 0) {
      elements.fileTreeContainer.innerHTML = `
        <div style="padding:1.5rem; text-align:center; color:var(--text-muted);">
          <p>No catalog files found.</p>
          <p style="font-size:0.75rem; margin-top:0.5rem;">Run <code>python generate_catalog.py</code> to build.</p>
        </div>
      `;
      return;
    }

    updateFileCountBadge();
    renderFileTree();

    // Default select a featured file
    const preferredFiles = [
      'chapter7_oop_advanced.py',
      'chapter8_iterators_generators.py',
      'chapter1_syntax_basics.py',
      '1helloWorld.py'
    ];
    let defaultFile = state.catalog.find(f => preferredFiles.includes(f.name));
    if (!defaultFile) defaultFile = state.catalog[0];

    if (defaultFile) {
      selectFile(defaultFile);
    }
  }

  // --- Render File Explorer Tree ---
  function updateFileCountBadge() {
    if (elements.fileCounterLabel) {
      elements.fileCounterLabel.textContent = `${state.catalog.length} Files Indexed`;
    }
  }

  function renderFileTree() {
    const query = state.searchQuery.trim().toLowerCase();
    const activeCat = state.activeCategory;

    // Filter files
    const filteredFiles = state.catalog.filter(file => {
      // Category filter
      if (activeCat !== 'all' && file.category !== activeCat) {
        return false;
      }
      // Search filter
      if (query) {
        const matchesName = file.name.toLowerCase().includes(query);
        const matchesPath = file.path.toLowerCase().includes(query);
        const matchesCategory = file.category.toLowerCase().includes(query);
        return matchesName || matchesPath || matchesCategory;
      }
      return true;
    });

    if (filteredFiles.length === 0) {
      elements.fileTreeContainer.innerHTML = `
        <div style="padding: 2rem 1rem; text-align: center; color: var(--text-dim); font-size: 0.82rem;">
          No matching files found.
        </div>
      `;
      return;
    }

    // Group by category
    const groups = {};
    for (const file of filteredFiles) {
      const cat = file.category || 'Other Code';
      if (!groups[cat]) groups[cat] = [];
      groups[cat].push(file);
    }

    let html = '';
    const categoryOrder = [
      'Core Fundamentals',
      'Advanced Masterclasses',
      'Data Science & Packages',
      'Lab Practicals & Exams',
      'Projects & Applications',
      'Other Code'
    ];

    const sortedCats = Object.keys(groups).sort((a, b) => {
      const idxA = categoryOrder.indexOf(a);
      const idxB = categoryOrder.indexOf(b);
      return (idxA !== -1 ? idxA : 99) - (idxB !== -1 ? idxB : 99);
    });

    for (const cat of sortedCats) {
      const files = groups[cat];
      html += `
        <div class="category-group">
          <div class="category-header">
            <span>${escapeHtml(cat)}</span>
            <span class="cat-count">${files.length}</span>
          </div>
          <div class="category-files">
      `;

      for (const file of files) {
        const isActive = state.activeFile && state.activeFile.path === file.path;
        const isModified = state.modifiedFiles.has(file.path);
        const icon = file.language === 'python' ? '🐍' : '📄';

        html += `
          <div class="file-item ${isActive ? 'active' : ''}" data-path="${escapeHtml(file.path)}">
            <div class="file-left">
              <span class="file-icon" style="font-size:0.85rem;">${icon}</span>
              <span class="file-name" title="${escapeHtml(file.path)}">${escapeHtml(file.name)}</span>
              ${isModified ? '<span class="status-dot" style="width:5px;height:5px;background:var(--amber);" title="Modified"></span>' : ''}
            </div>
            <span class="file-lines">${file.lines || 0}L</span>
          </div>
        `;
      }

      html += `
          </div>
        </div>
      `;
    }

    elements.fileTreeContainer.innerHTML = html;

    // Attach click listeners to file items
    elements.fileTreeContainer.querySelectorAll('.file-item').forEach(item => {
      item.addEventListener('click', () => {
        const path = item.getAttribute('data-path');
        const targetFile = state.catalog.find(f => f.path === path);
        if (targetFile) selectFile(targetFile);
      });
    });
  }

  // --- Select & Load File in Editor ---
  function selectFile(file) {
    state.activeFile = file;

    // Update active tab & UI headers
    if (elements.activeFileTitle) {
      elements.activeFileTitle.textContent = file.name;
    }

    // Determine content (modified or original)
    const content = state.modifiedFiles.has(file.path)
      ? state.modifiedFiles.get(file.path)
      : file.content;

    elements.codeTextarea.value = content;
    updateLineNumbers();
    updateModifiedIndicator();

    // Update active highlight in sidebar
    elements.fileTreeContainer.querySelectorAll('.file-item').forEach(el => {
      if (el.getAttribute('data-path') === file.path) {
        el.classList.add('active');
        el.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      } else {
        el.classList.remove('active');
      }
    });

    // Reset editor scroll
    elements.codeTextarea.scrollTop = 0;
    elements.codeTextarea.scrollLeft = 0;
    elements.lineNumbers.scrollTop = 0;
  }

  // --- Update Line Numbers ---
  function updateLineNumbers() {
    const lines = elements.codeTextarea.value.split('\n').length;
    let nums = '';
    for (let i = 1; i <= lines; i++) {
      nums += i + '\n';
    }
    elements.lineNumbers.textContent = nums;
  }

  function updateModifiedIndicator() {
    if (!state.activeFile) return;
    const isModified = state.modifiedFiles.has(state.activeFile.path);
    if (elements.modifiedIndicator) {
      elements.modifiedIndicator.style.display = isModified ? 'inline-block' : 'none';
    }
  }

  // --- Editor Input Handlers ---
  elements.codeTextarea.addEventListener('input', () => {
    updateLineNumbers();
    if (!state.activeFile) return;

    const currentVal = elements.codeTextarea.value;
    if (currentVal !== state.activeFile.content) {
      state.modifiedFiles.set(state.activeFile.path, currentVal);
    } else {
      state.modifiedFiles.delete(state.activeFile.path);
    }
    updateModifiedIndicator();
  });

  // Sync scroll between textarea and line numbers
  elements.codeTextarea.addEventListener('scroll', () => {
    elements.lineNumbers.scrollTop = elements.codeTextarea.scrollTop;
  });

  // Handle Tab key indentation in editor
  elements.codeTextarea.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = elements.codeTextarea.selectionStart;
      const end = elements.codeTextarea.selectionEnd;
      const val = elements.codeTextarea.value;
      const spaces = '    ';

      elements.codeTextarea.value = val.substring(0, start) + spaces + val.substring(end);
      elements.codeTextarea.selectionStart = elements.codeTextarea.selectionEnd = start + spaces.length;

      // Trigger input event to update line numbers and modification state
      elements.codeTextarea.dispatchEvent(new Event('input'));
    } else if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      // Ctrl+Enter or Cmd+Enter executes code
      e.preventDefault();
      executeActiveCode();
    }
  });

  // --- Editor Toolbar Actions ---
  elements.btnResetCode.addEventListener('click', () => {
    if (!state.activeFile) return;
    state.modifiedFiles.delete(state.activeFile.path);
    elements.codeTextarea.value = state.activeFile.content;
    updateLineNumbers();
    updateModifiedIndicator();
    showToast(`Reverted "${state.activeFile.name}" to original`);
  });

  elements.btnCopyCode.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(elements.codeTextarea.value);
      showToast('Code copied to clipboard!');
    } catch (err) {
      showToast('Failed to copy code to clipboard');
    }
  });

  elements.btnDownloadCode.addEventListener('click', () => {
    if (!state.activeFile) return;
    const blob = new Blob([elements.codeTextarea.value], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = state.activeFile.name;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast(`Downloaded ${state.activeFile.name}`);
  });

  // --- Copy Git Clone Command ---
  elements.btnCopyClone.addEventListener('click', async () => {
    const cmd = 'git clone https://github.com/Ken-Kanike/Python.git';
    try {
      await navigator.clipboard.writeText(cmd);
      showToast('Copied: ' + cmd);
    } catch {
      showToast('Clone command: ' + cmd);
    }
  });

  // --- Search & Filtering ---
  elements.searchInput.addEventListener('input', () => {
    state.searchQuery = elements.searchInput.value;
    elements.btnClearSearch.style.display = state.searchQuery ? 'inline-block' : 'none';
    renderFileTree();
  });

  elements.btnClearSearch.addEventListener('click', () => {
    elements.searchInput.value = '';
    state.searchQuery = '';
    elements.btnClearSearch.style.display = 'none';
    renderFileTree();
  });

  elements.categoryChips.forEach(chip => {
    chip.addEventListener('click', () => {
      elements.categoryChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      state.activeCategory = chip.getAttribute('data-cat');
      renderFileTree();
    });
  });

  elements.btnRefreshCatalog.addEventListener('click', () => {
    showToast('Refreshing catalog...');
    loadCatalog();
  });

  // --- Terminal Output Helpers ---
  function appendTerminalLine(text, type = 'stdout') {
    const line = document.createElement('div');
    line.className = `terminal-line ${type}`;

    if (type === 'system') {
      line.innerHTML = `<span class="prompt-symbol">>>></span> ${escapeHtml(text)}`;
    } else if (type === 'repl-in') {
      line.innerHTML = `<span class="prompt-symbol" style="color:var(--py-gold);">>>></span> <code>${escapeHtml(text)}</code>`;
    } else {
      line.textContent = text;
    }

    elements.terminalBody.appendChild(line);
    elements.terminalBody.scrollTop = elements.terminalBody.scrollHeight;
  }

  function appendTerminalPlot(imgDataUrl) {
    const container = document.createElement('div');
    container.style.padding = '0.5rem 0';
    container.style.maxWidth = '100%';

    const img = document.createElement('img');
    img.src = imgDataUrl;
    img.style.maxWidth = '100%';
    img.style.maxHeight = '320px';
    img.style.borderRadius = '6px';
    img.style.border = '1px solid var(--border-subtle)';
    img.style.boxShadow = '0 4px 12px rgba(0,0,0,0.5)';

    container.appendChild(img);
    elements.terminalBody.appendChild(container);
    elements.terminalBody.scrollTop = elements.terminalBody.scrollHeight;
  }

  elements.btnClearTerminal.addEventListener('click', () => {
    elements.terminalBody.innerHTML = `
      <div class="terminal-welcome-msg">
        <span class="prompt-symbol">>>></span> Console cleared. Ready for execution.
      </div>
    `;
    elements.executionTimeBadge.style.display = 'none';
  });

  // --- REPL Toggle & Execution ---
  elements.btnToggleRepl.addEventListener('click', () => {
    const isHidden = elements.replBar.style.display === 'none';
    elements.replBar.style.display = isHidden ? 'flex' : 'none';
    elements.btnToggleRepl.classList.toggle('active', isHidden);
    if (isHidden) {
      elements.replInput.focus();
    }
  });

  async function executeReplExpression() {
    const expr = elements.replInput.value.trim();
    if (!expr) return;

    if (!state.pyodide) {
      appendTerminalLine('Pyodide WebAssembly runtime is still initializing. Please wait...', 'stderr');
      return;
    }

    // Add to REPL history
    state.replHistory.push(expr);
    state.replHistoryIndex = state.replHistory.length;
    elements.replInput.value = '';

    appendTerminalLine(expr, 'repl-in');

    const startTime = performance.now();
    try {
      // Evaluate in Pyodide
      const result = await state.pyodide.runPythonAsync(expr);
      const elapsed = Math.round(performance.now() - startTime);

      if (result !== undefined) {
        appendTerminalLine(String(result), 'stdout');
      }
      elements.executionTimeBadge.textContent = `⚡ ${elapsed}ms`;
      elements.executionTimeBadge.style.display = 'inline-block';
    } catch (err) {
      appendTerminalLine(err.message, 'stderr');
    }
  }

  elements.btnSubmitRepl.addEventListener('click', executeReplExpression);

  elements.replInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      executeReplExpression();
    } else if (e.key === 'ArrowUp') {
      if (state.replHistory.length > 0 && state.replHistoryIndex > 0) {
        state.replHistoryIndex--;
        elements.replInput.value = state.replHistory[state.replHistoryIndex];
      }
    } else if (e.key === 'ArrowDown') {
      if (state.replHistoryIndex < state.replHistory.length - 1) {
        state.replHistoryIndex++;
        elements.replInput.value = state.replHistory[state.replHistoryIndex];
      } else {
        state.replHistoryIndex = state.replHistory.length;
        elements.replInput.value = '';
      }
    }
  });

  // --- Synchronize Virtual Filesystem in Pyodide ---
  function syncVFS() {
    if (!state.pyodide || !state.catalog) return;

    for (const file of state.catalog) {
      try {
        const parts = file.path.split('/');
        if (parts.length > 1) {
          let curr = '';
          for (let i = 0; i < parts.length - 1; i++) {
            curr += (curr ? '/' : '') + parts[i];
            try {
              state.pyodide.FS.mkdir(curr);
            } catch (e) {
              // Directory may already exist
            }
          }
        }

        // Get updated or original content
        const content = state.modifiedFiles.has(file.path)
          ? state.modifiedFiles.get(file.path)
          : file.content;

        state.pyodide.FS.writeFile(file.path, content, { encoding: 'utf8' });
      } catch (err) {
        // Suppress VFS write failures for non-critical files
      }
    }
  }

  // --- Initialize Pyodide Runtime ---
  async function initPyodide() {
    if (typeof loadPyodide === 'undefined') {
      console.warn('Pyodide script failed to load from CDN.');
      elements.runtimeBadge.className = 'status-pill status-loading';
      elements.runtimeBadge.style.borderColor = 'var(--crimson)';
      elements.runtimeText.textContent = 'Pyodide Offline (CDN unreachable)';
      state.isPyodideLoading = false;
      return;
    }

    try {
      elements.runtimeBadge.className = 'status-pill status-loading';
      elements.runtimeText.textContent = 'Loading CPython 3.12 WebAssembly...';

      state.pyodide = await loadPyodide({
        stdout: (text) => appendTerminalLine(text, 'stdout'),
        stderr: (text) => appendTerminalLine(text, 'stderr'),
      });

      // Synchronize repository files to Pyodide virtual filesystem
      syncVFS();

      // Configure matplotlib hook if matplotlib is imported
      await state.pyodide.runPythonAsync(`
import sys
import io

# Setup plotting helper hook if matplotlib is used
def _capture_plot_figures():
    try:
        import matplotlib.pyplot as plt
        figs = [plt.figure(n) for n in plt.get_fignums()]
        if not figs:
            return []
        import base64
        results = []
        for fig in figs:
            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            img_b64 = base64.b64encode(buf.read()).decode('ascii')
            results.append("data:image/png;base64," + img_b64)
            plt.close(fig)
        return results
    except Exception:
        return []
`);

      elements.runtimeBadge.className = 'status-pill status-ready';
      elements.runtimeText.textContent = 'Python 3.12 Ready (Client-side WASM)';
      state.isPyodideLoading = false;
    } catch (err) {
      console.error('Failed to initialize Pyodide:', err);
      elements.runtimeBadge.className = 'status-pill status-loading';
      elements.runtimeBadge.style.borderColor = 'var(--crimson)';
      elements.runtimeText.textContent = 'Pyodide Initialization Failed';
      state.isPyodideLoading = false;
    }
  }

  // --- Run Active File Code in Browser ---
  async function executeActiveCode() {
    if (state.isExecuting) return;

    if (!state.pyodide) {
      if (state.isPyodideLoading) {
        showToast('WebAssembly Python runtime is still loading, please wait a moment...');
      } else {
        showToast('Pyodide runtime is not available in this environment.');
      }
      return;
    }

    const code = elements.codeTextarea.value;
    if (!code.trim()) {
      showToast('No code to execute');
      return;
    }

    state.isExecuting = true;
    elements.btnRunCode.disabled = true;
    elements.runButtonText.textContent = 'Running...';
    elements.runtimeBadge.className = 'status-pill status-running';
    elements.runtimeText.textContent = 'Executing Python code...';

    // Print starting banner in terminal
    const fileName = state.activeFile ? state.activeFile.name : 'script.py';
    appendTerminalLine(`Executing ${fileName}...`, 'system');

    // Sync active file changes to Pyodide VFS before running
    if (state.activeFile) {
      try {
        state.pyodide.FS.writeFile(state.activeFile.path, code, { encoding: 'utf8' });
      } catch (e) {
        // Ignore VFS write error
      }
    }

    const startTime = performance.now();

    try {
      // Auto-load third-party packages if imported (e.g. numpy, matplotlib)
      try {
        await state.pyodide.loadPackagesFromImports(code);
      } catch (pkgErr) {
        // Continue even if package auto-load throws (might be a local module)
      }

      // Execute code
      await state.pyodide.runPythonAsync(code);

      // Check for generated matplotlib plots
      try {
        const plotImages = await state.pyodide.runPythonAsync('_capture_plot_figures()');
        if (plotImages && plotImages.toJs) {
          const imgs = plotImages.toJs();
          for (const imgUrl of imgs) {
            appendTerminalPlot(imgUrl);
          }
        }
      } catch (plotErr) {
        // Ignore plot capture errors
      }

      const elapsed = Math.round(performance.now() - startTime);
      elements.executionTimeBadge.textContent = `⚡ ${elapsed}ms`;
      elements.executionTimeBadge.style.display = 'inline-block';
      appendTerminalLine(`Program finished in ${elapsed}ms`, 'system');
    } catch (err) {
      appendTerminalLine(err.message, 'stderr');
      const elapsed = Math.round(performance.now() - startTime);
      elements.executionTimeBadge.textContent = `⚡ ${elapsed}ms (Error)`;
      elements.executionTimeBadge.style.display = 'inline-block';
    } finally {
      state.isExecuting = false;
      elements.btnRunCode.disabled = false;
      elements.runButtonText.textContent = 'Run in Browser';
      elements.runtimeBadge.className = 'status-pill status-ready';
      elements.runtimeText.textContent = 'Python 3.12 Ready (Client-side WASM)';
    }
  }

  elements.btnRunCode.addEventListener('click', executeActiveCode);

  // --- Initialize App ---
  async function init() {
    await loadCatalog();
    initPyodide();
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
