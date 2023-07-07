SELECT b.name, COUNT(*) AS receipts_scanned
FROM Brands b
JOIN RewardsReceiptItemList ri ON b.barcode = ri.barcode
JOIN Receipts r ON ri.receiptId = r._id
WHERE MONTH(r.dateScanned) = MONTH(CURRENT_DATE()) AND YEAR(r.dateScanned) = YEAR(CURRENT_DATE())
GROUP BY b.name
ORDER BY receipts_scanned DESC
LIMIT 5;
