import os
import pytest
from pathlib import Path

# Add the project root to Python path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from text_analyzer import text_reader, list_available_files

@pytest.fixture
def temp_files(tmp_path):
    """Create temporary test files"""
    files_dir = tmp_path / "files"
    files_dir.mkdir()
    
    # Test files with different content
    test_files = {
        "empty.txt": ""
    }
    
    # Create files
    for filename, content in test_files.items():
        file_path = files_dir / filename
        file_path.write_text(content, encoding='utf-8')
    
    return str(files_dir)

@pytest.fixture
def mock_files_dir(monkeypatch, temp_files):
    """Mock the files directory operations"""
    def mock_listdir(path):
        if path == "files":
            return ["empty.txt"]
        return os.listdir(path)
    
    def mock_exists(path):
        if path == "files":
            return True
        return os.path.exists(path)
    
    def mock_join(*args):
        if args[0] == "files":
            return os.path.join(temp_files, *args[1:])
        return os.path.join(*args)
    
    # Apply mocks
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(os.path, 'join', mock_join)

def test_text_reader_empty_file(temp_files):
    """Test text_reader function with empty file"""
    file_path = os.path.join(temp_files, "empty.txt")
    result = text_reader(file_path)
    
    assert result is not None
    assert result['word_count'] == 0
    assert result['sentence_count'] == 0

def test_text_reader_file_not_found():
    """Test text_reader with non-existent file"""
    result = text_reader("nonexistent.txt")
    assert result is None

def test_list_available_files(mock_files_dir):
    """Test list_available_files function"""
    files = list_available_files()
    
    assert len(files) == 1
    assert all(f.endswith('.txt') for f in files)
    assert "empty.txt" in files 