import subprocess

def convert_notebook_to_pdf(notebook_path, output_path=None):
    """
    Convert a Jupyter Notebook to a PDF file.

    Parameters:
    - notebook_path: str, path to the .ipynb file
    - output_path: str, path to save the output PDF file (optional)
    """
    command = ['jupyter', 'nbconvert', '--to', 'pdf', notebook_path]
    
    if output_path:
        command.extend(['--output', output_path])
    
    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted {notebook_path} to PDF.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {notebook_path} to PDF: {e}")
        print(f"Command output: {e.output}")

# Example usage
notebook_path = '5025221299_5025221156_5025221158.ipynb'
output_path = '5025221299_5025221156_5025221158.pdf'  # Optional, specify if you want a custom output path

convert_notebook_to_pdf(notebook_path, output_path)