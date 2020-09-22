Attribute VB_Name = "Module1"
Public Sub MacroTest10() 'Beginning of program

'Set main worksheet as worksheet object variable
Dim ws As Worksheet
Dim wb As Workbook
Dim headers() As Variant
Dim i As Integer

'Set current workbook to alias for ease of commands
Set wb = ActiveWorkbook

'Define header information on each worksheet
headers() = Array("Ticker", "Date ", "Open", "High", "Low", "Close", "Volume", " ", "Ticker", "Yearly_Change", "Percent_Change", "Stock_Volume", " ", " ", " ", "Ticker", "Value")
    
'For loop through worksheets in workbook for header set-up
For Each ws In wb.Sheets
    With ws 'With loop allows disregarding alias for worksheet shared between commands
         .Rows(1).Value = " " 'Clears current cell
        
    For i = LBound(headers()) To UBound(headers()) 'For loop through header array
        .Cells(1, 1 + i).Value = headers(i) 'Add header titles for each column
    
    Next i 'For loop step into next header index

        .Rows(1).Font.Bold = True 'Format header as bold
        .Rows(1).VerticalAlignment = xlCenter 'Format header at center justification
    
    End With 'With loop termination
    
Next ws 'For loop step into next worksheet index
'******************************************************
'For Loop through worksheets in workbook for stock calculations
For Each ws In Worksheets
    
    'Set initial variables for calculations
        Dim Ticker_Name As String
        Ticker_Name = " "
        Dim Total_Ticker_Volume As Double
        Total_Ticker_Volume = 0
        Dim Beg_Price As Double
        Beg_Price = 0
        Dim End_Price As Double
        End_Price = 0
        Dim Yearly_Price_Change As Double
        Yearly_Price_Change = 0
        Dim Yearly_Price_Change_Percent
        Yearly_Price_Change_Percent = 0
        Dim Max_Ticker_Name As String
        Max_Ticker_Name = " "
        Dim Min_Ticker_Name As String
        Min_Ticker_Name = " "
        Dim Max_Percent As Double
        Max_Percent = 0
        Dim Min_Percent As Double
        Min_Percent = 0
        Dim Max_Volume_Ticker_Name As String
        Max_Volume_Ticker_Name = " "
        Dim Max_Volume As Double
        Max_Volume = 0
        
    '******************************************************
    
    'Set location for variables
    Dim Summary_Table_Row As Long
    Summary_Table_Row = 2
    
    'Set row count for all sheets in the workbook
    Dim Lastrow As Long
    
    'Loop through all sheets to find last cell that isnt empty
    Lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    'Set initial value of beginning stock value for the first Ticker of ws
    Beg_Price = ws.Cells(2, 3).Value
    
    'Loop from the beginning of the main worksheet row 2 until last row of last worksheet
    For o = 2 To Lastrow
    
        'Check confirmation on same ticker name
        If ws.Cells(o + 1, 1).Value <> ws.Cells(o, 1).Value Then
        
            'Set the ticker name starting point
            Ticker_Name = ws.Cells(o, 1).Value
            
            'Calculate yearly price change
            End_Price = ws.Cells(o, 6).Value
            Yearly_Price_Change = End_Price - Beg_Price
            
            'Set condition for a zero value
            If Beg_Price <> 0 Then
                Yearly_Price_Change_Percent = (Yearly_Price_Change / Beg_Price) * 100
                
            End If 'If statement termination
            
            'Calculate the Ticker Name Total Volume
            Total_Ticker_Volume = Total_Ticker_Volume + ws.Cells(o, 7).Value
            
            'Print Ticker Name in Summary Table, Column I
            ws.Range("I" & Summary_Table_Row).Value = Ticker_Name
            
            'Print the yearly price change in the Summary Table, Column J
            ws.Range("J" & Summary_Table_Row).Value = Yearly_Price_Change
            
            'Conditional format Yearly Price Change to red for negative and green for positive
            If (Yearly_Price_Change > 0) Then
                ws.Range("J" & Summary_Table_Row).Interior.ColorIndex = 4
            
            ElseIf (Yearly_Price_Change <= 0) Then
                ws.Range("J" & Summary_Table_Row).Interior.ColorIndex = 3
                
            End If 'If statement termination
            
            'Calculate the yearly price change as percent in the Summary Table Column K
            ws.Range("K" & Summary_Table_Row).Value = (CStr(Yearly_Price_Change_Percent) & "%")
            
            'Calculate total stock volume in the Summary Table Column L
            ws.Range("L" & Summary_Table_Row).Value = Total_Ticker_Volume
            
            'Add 1 to Summary table row count
            Summary_Table_Row = Summary_Table_Row + 1
            
            'Get next beginning price
            Beg_Price = ws.Cells(o + 1, 3).Value
            
            'Calculate worksheet percentage changes
            If (Yearly_Price_Change_Percent > Max_Percent) Then
                Max_Percent = Yearly_Price_Change_Percent
                Max_Ticker_Name = Ticker_Name
                
            ElseIf (Yearly_Price_Change_Percent < Min_Percent) Then
                Min_Percent = Yearly_Price_Change_Percent
                Min_Ticker_Name = Ticker_Name
                
            End If 'If statement termination
            
            If (Total_Ticker_Volume > Max_Volume) Then
                Max_Volume = Total_Ticker_Volume
                Max_Volume_Ticker_Name = Ticker_Name
                
            End If 'If statement termination
            
            'Reset Values
            Yearly_Price_Change_Percent = 0
            Total_Ticker_Volume = 0
            
        'Else If in next ticker name then enter new ticker stock volume
        Else
            Total_Ticker_Volume = Total_Ticker_Volume + ws.Cells(o, 7).Value
            
        End If 'If statement termination
        
    Next o 'For loop step into next row index
    
        'Input values in assigned cells
        ws.Range("O2").Value = "Greatest % Increase"
        ws.Range("O3").Value = "Greatest % Decrease"
        ws.Range("O4").Value = "Greatest Total Volume"
        ws.Range("P2").Value = Max_Ticker_Name
        ws.Range("P3").Value = Min_Ticker_Name
        ws.Range("P4").Value = Max_Volume_Ticker_Name
        ws.Range("Q2").Value = (CStr(Max_Percent) & "%")
        ws.Range("Q3").Value = (CStr(Min_Percent) & "%")
        ws.Range("Q4").Value = Max_Volume
        
        'Autofit all columns within worksheet for presentation
        ws.Cells.Columns.AutoFit
        
Next ws 'For loop step into next worksheet index

End Sub 'End of program
